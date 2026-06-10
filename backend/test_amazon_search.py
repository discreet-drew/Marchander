import asyncio

from app.scrapers.amazon_search import (
    search_amazon
)

result = asyncio.run(
    search_amazon(
        "iphone 15"
    )
)

print(result)