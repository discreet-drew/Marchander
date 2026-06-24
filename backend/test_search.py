import asyncio

from app.scrapers.Electronics.flipkart_search import (
    search_flipkart
)

result = asyncio.run(
    search_flipkart(
        "iphone 15"
    )
)

print(result)