import asyncio

from app.scrapers.amazon import (
    scrape_amazon
)

from app.scrapers.amazon_search import (
    search_amazon
)

query = "iphone 15"

url = asyncio.run(
    search_amazon(query)
)

print(
    "Found URL:",
    url
)

result = scrape_amazon(
    url
)

print(result)