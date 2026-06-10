import re

from playwright.sync_api import sync_playwright #type: ignore


def scrape_amazon(url):

    with sync_playwright() as p:

        browser = p.chromium.launch(
            headless=False
        )

        page = browser.new_page()

        page.set_extra_http_headers({
    "Accept-Language": "en-IN,en;q=0.9"
})
        
        browser = p.chromium.launch(
    headless=False,
    slow_mo=100
)

        page.goto(
            url,
            wait_until="commit",
            timeout=60000
    )
        page.wait_for_timeout(3000)

        html = page.content()

        browser.close()

        title_match = re.search(
            r'<title>(.*?)</title>',
            html,
            re.DOTALL
        )

        title = (
            title_match.group(1)
            if title_match
            else "Unknown"
        )

        price = None

        patterns = [

            r'"price":"([\d,.]+)"',

            r'priceToPay.*?a-offscreen">₹([\d,]+)',

            r'a-price-whole">([\d,]+)'
        ]

        for pattern in patterns:

            match = re.search(
                pattern,
                html
            )

            if match:

                price = match.group(1)

                break

        return {

            "store": "Amazon",

            "title": title,

            "price": price,

            "currency": "INR"
        }
    
    availability = "Unknown"
    if (
        "In Stock" in html
        or
        "in stock" in html.lower()
    ):
        availability = "In Stock"

    elif (
        "Currently unavailable"
        in html
    ):
        availability = (
            "Out of Stock"
        )

        return {

    "store":"Amazon",

    "title":title,

    "price":price,

    "currency":"INR",

    "availability":
    availability
}