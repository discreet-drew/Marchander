from playwright.async_api import (
    async_playwright
)

async def search_amazon(
    query
):

    search_url = (

        "https://www.amazon.in/s?k="

        +

        query.replace(
            " ",
            "+"
        )
    )

    async with async_playwright() as p:

        browser = (
            await p.chromium.launch(
                headless=False
            )
        )

        page = (
            await browser.new_page()
        )

        await page.goto(
            search_url,
            wait_until=
            "domcontentloaded"
        )

        await page.wait_for_timeout(
            5000
        )

        products = (
            await page.locator(
                'a[href*="/dp/"]'
            ).all()
        )

        for product in products:

            href = (
                await product.get_attribute(
                    "href"
                )
            )

            if href:

                await browser.close()

                if href.startswith(
                    "http"
                ):
                    return href

                return (
                    "https://www.amazon.in"
                    + href
                )

        await browser.close()

        return None