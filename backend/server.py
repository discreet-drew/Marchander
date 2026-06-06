from flask import Flask, request, jsonify
from flask_cors import CORS

import asyncio

from app.scrapers.flipkart import (
    scrape_flipkart
)

from app.scrapers.flipkart_search import (
    search_flipkart
)

app = Flask(__name__)

CORS(app)


@app.route("/")
def home():

    return {
        "message":
        "Marchander Running"
    }


@app.route(
    "/search",
    methods=["POST"]
)
def search():

    data = request.get_json()

    query = data["query"]

    print(
        "Searching:",
        query
    )

    product_url = asyncio.run(
        search_flipkart(query)
    )

    print(
        "URL:",
        product_url
    )

    if not product_url:

        return jsonify({
            "error":
            "Product not found"
        })

    product = scrape_flipkart(
        product_url
    )

    print(
        "Product:",
        product
    )

    return jsonify(product)


if __name__ == "__main__":

    app.run(
        debug=True,
        port=5000
    )