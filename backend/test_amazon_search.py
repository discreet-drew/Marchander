# test_amazon_search.py

import asyncio

from app.scrapers.Electronics.amazon_search import (
    search_amazon
)

url = asyncio.run(
    search_amazon(
        "iphone 15"
    )
)

print(url)