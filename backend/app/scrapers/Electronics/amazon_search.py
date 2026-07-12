from playwright.async_api import async_playwright


async def search_amazon(query):

    search_url = (
        "https://www.amazon.in/s?k="
        + query.replace(" ", "+")
    )

    async with async_playwright() as p:

        browser = await p.chromium.launch(headless=True)

        page = await browser.new_page()

        await page.goto(
            search_url,
            wait_until="domcontentloaded",
            timeout=30000
        )

        await page.wait_for_timeout(3000)

        products = page.locator(
            '[data-component-type="s-search-result"]'
        )

        count = await products.count()

        print(f"Products Found: {count}")

        query_lower = query.lower()

        for i in range(count):

            try:

                product = products.nth(i)

                title = await product.locator(
                    "h2.a-size-medium"
                ).first.inner_text()

                print(
                    "Candidate:",
                    title
                )

                link = await product.locator(
                    "a.a-link-normal"
                ).first.get_attribute(
                    "href"
                )

                if link:

                    await browser.close()

                    if link.startswith(
                        "http"
                    ):
                        return link

                    return (
                        "https://www.amazon.in"
                        + link
                    )

            except Exception as e:

                print(
                    "ERROR:",
                    e
                )

        await browser.close()

        return None