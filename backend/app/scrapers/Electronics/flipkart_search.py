from playwright.sync_api import sync_playwright # type: ignore
import asyncio


def _sync_search_flipkart(query: str):
    url = "https://www.flipkart.com/search?q=" + query.replace(" ", "+")

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        
        
        page = browser.new_page()
        page.goto(url, wait_until="domcontentloaded")
        page.wait_for_timeout(5000)

        links = page.locator("a").evaluate_all(
            "elements => elements.map(e => e.href)"
        )

        browser.close()

        for link in links:
            if "/p/" in link:
                return link

        return None


async def search_flipkart(query: str):
    loop = asyncio.get_running_loop()
    return await loop.run_in_executor(None, _sync_search_flipkart, query)