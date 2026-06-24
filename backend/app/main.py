import asyncio
import sys

if sys.platform.startswith("win"):
    asyncio.set_event_loop_policy(asyncio.WindowsProactorEventLoopPolicy())

from fastapi import FastAPI  # type: ignore

from app.schemas import (
    SearchRequest
)

from app.scrapers.Electronics.flipkart import (
    scrape_flipkart
)


import asyncio
import sys

if sys.platform.startswith("win"):
    asyncio.set_event_loop_policy(
        asyncio.WindowsProactorEventLoopPolicy()
    )

from app.scrapers.Electronics.flipkart_search import (
    search_flipkart
)

app = FastAPI()


@app.post("/search-product")
async def search_product(request: SearchRequest):

    try:

        print("Query:", request.query)

        product_url = await search_flipkart(
            request.query
        )

        print("Product URL:", product_url)

        product =  scrape_flipkart(
            product_url
        )

        print("Product:", product)

        return product

    except Exception as e:

        print("ERROR:", str(e))

        import traceback
        traceback.print_exc()

        return {
            "error": str(e)
        }