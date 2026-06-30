from flask import Flask, request, jsonify #type: ignore
from flask_cors import CORS  #type: ignore

import asyncio
from app.ai.recommender import suggest_products


from app.services.history_service import (
    save_price,
    get_product_analytics
)


from app.scrapers.Electronics.flipkart import scrape_flipkart
from app.scrapers.Electronics.flipkart_search import search_flipkart

from app.scrapers.Electronics.amazon import scrape_amazon
from app.scrapers.Electronics.amazon_search import search_amazon

from app.comparison import compare_prices

app = Flask(__name__)

CORS(app)


@app.route("/")
def home():

    return {
        "message": "Marchander Running"
    }


@app.route(
    "/search",
    methods=["POST"]
)

@app.route(

    "/history/<product>",

    methods=["GET"]

)

@app.route("/recommend")
def recommend():

    query = request.args.get("query")

    recommendations = suggest_products(query)

    return jsonify([
        {
            "product": product,
            "score": round(score, 4)
        }
        for product, score in recommendations
    ])

def history(product):

    analytics = get_product_analytics(

        product

    )

    history = []

    for row in analytics["history"]:

        history.append(

            {

                "store": row[0],

                "price": row[1],

                "date": row[2].strftime(

                    "%Y-%m-%d %H:%M"

                )

            }

        )

    return jsonify(

        {

            "product": product,

            "current_price":

                analytics["current_price"],

            "lowest_price":

                analytics["lowest_price"],

            "highest_price":

                analytics["highest_price"],

            "average_price":

                analytics["average_price"],

            "history":

                history

        }

    )

def search():
    try:
        data = request.get_json()
        query = data["query"]
        print(f"\nSearching: {query}")

        # Flipkart
        flipkart_product = None
        try:
            flipkart_url = asyncio.run(search_flipkart(query))
            print("Flipkart URL:", flipkart_url)
            if flipkart_url:
                flipkart_product = scrape_flipkart(flipkart_url)

            if ( flipkart_product and flipkart_product["price"]):

                save_price(

                    flipkart_product["title"],

                    "Flipkart",

                    flipkart_product["price"],

                    flipkart_url)
        
        except Exception as e:
            print("Flipkart Error:", e)
            flipkart_product = {
                "store": "Flipkart",
                "title": "Unavailable",
                "price": None,
                "currency": "INR",
                "availability": "Unavailable",
            }

        # Amazon
        amazon_product = None
        try:
            amazon_url = asyncio.run(search_amazon(query))
            print("Amazon URL:", amazon_url)
            if amazon_url:
                amazon_product = scrape_amazon(amazon_url)

            if (amazon_product and amazon_product["price"]):

                save_price(

                    amazon_product["title"],

                    "Amazon",

                    amazon_product["price"],

                    amazon_url

             )
        except Exception as e:
            print("Amazon Error:", e)
            amazon_product = {
                "store": "Amazon",
                "title": "Unavailable",
                "price": None,
                "currency": "INR",
                "availability": "Unavailable",
            }

        # Comparison
        comparison = None
        try:
            comparison = compare_prices(flipkart_product, amazon_product)
        except Exception:
            comparison = None

        print("Flipkart Product:", flipkart_product)
        print("Amazon Product:", amazon_product)
        print("Comparison:", comparison)

        return jsonify(comparison)
    

        saved = None

        if (

        flipkart_product

        and

        amazon_product

        ):

            if (

                flipkart_product["price"]

                <

                amazon_product["price"]

            ):

                saved = (

                    amazon_product["price"]

                    -

                    flipkart_product["price"]

            )

    except Exception as e:
        print("Search Error:", e)
        return jsonify({"error": "Search failed"}), 500


if __name__ == "__main__":

    app.run(
        debug=True,
        port=5000
    )
