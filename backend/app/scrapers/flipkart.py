import json

from playwright.sync_api import sync_playwright #type: ignore


def scrape_flipkart(url):

    with sync_playwright() as p:

        browser = p.chromium.launch(
            headless=False
        )

        page = browser.new_page()

        page.goto(
            url,
            wait_until="domcontentloaded"
        )

        page.wait_for_timeout(5000)

        scripts = page.locator(
            'script[type="application/ld+json"]'
        ).all_text_contents()

        browser.close()

        for script in scripts:

            try:

                data = json.loads(script)

                if isinstance(data, list):

                    for item in data:

                        if "offers" in item:

                            return {
                                "store": "Flipkart",
                                "title": item["name"],
                                "price": item["offers"]["price"],
                                "currency": item["offers"]["priceCurrency"]
                            }

            except:
                pass

        return None