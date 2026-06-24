from playwright.sync_api import sync_playwright
import re

def scrape_amazon(url):

    with sync_playwright() as p:

        browser = p.chromium.launch(
            headless=True
        )

        page = browser.new_page()

        page.goto(
            url,
            wait_until="domcontentloaded",
            timeout=60000
        )

        page.wait_for_timeout(3000)

        title = page.title()

        price = None

        selectors = [

    ".a-price-whole",

    ".aok-offscreen",

    ".reinventPricePriceToPayMargin",

    "#corePriceDisplay_desktop_feature_div .a-price-whole",

    "#priceblock_ourprice",

    "#priceblock_dealprice"
]

        for selector in selectors:

            try:

                locator = page.locator(
                    selector
                ).first

                if locator.count() > 0:
                    text = locator.inner_text()

                match = re.search(
                    r'[\d,]+',
                    text
                )

                if match:

                    price = int(
                        match.group()
                        .replace(",", "")
                    )

                    break

            except:
                pass

        print(
            "Amazon Title:",
            title
        )

        print(
            "Amazon Price:",
            price
        )

        return {

            "store": "Amazon",

            "title": title,

            "price": price,

            "currency": "INR",

            "url": url
        }