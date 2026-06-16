from flask import Flask, request, jsonify
from flask_cors import CORS

import asyncio

from app.scrapers.flipkart import scrape_flipkart
from app.scrapers.flipkart_search import search_flipkart

from app.scrapers.amazon import scrape_amazon
from app.scrapers.amazon_search import search_amazon

from app.comparison import compare_prices
from app import comparison

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

        return jsonify({
            "flipkart": flipkart_product,
            "amazon": amazon_product,
            "comparison": comparison,
        })
    except Exception as e:
        print("Search Error:", e)
        return jsonify({"error": "Search failed"}), 500

if __name__ == "__main__":

    app.run(
        debug=True,
        port=5000
    )

    try:

        loop = asyncio.get_event_loop()
        loop.run_forever()
    except KeyboardInterrupt:

        pass 
    print("FINAL RESPONSE:", comparison)