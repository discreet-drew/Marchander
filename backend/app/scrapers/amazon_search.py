from playwright.async_api import async_playwright  # type: ignore


async def search_amazon(query):

    search_url = (
        "https://www.amazon.in/s?k="
        + query.replace(" ", "+")
    )

    async with async_playwright() as p:

        browser = await p.chromium.launch(
            headless=False
        )

        page = await browser.new_page()

        await page.goto(
            search_url,
            wait_until="domcontentloaded"
        )

        await page.wait_for_timeout(
            5000
        )

        products = page.locator(
            '[data-component-type="s-search-result"]'
        )

        count = await products.count()

        query_words = (
            query.lower()
            .replace("+", " ")
            .split()
        )

        for i in range(count):

            try:

                product = products.nth(i)

                title_locator = product.locator(
                    "h2"
                )

                title = (
                    await title_locator
                    .inner_text()
                )

                title_lower = (
                    title.lower()
                )

                # Match query words

                matches = 0

                for word in query_words:

                    if word in title_lower:
                        matches += 1

                # Require most words to match

                if matches >= max(
                    1,
                    len(query_words) - 1
                ):

                    link = (
                        await product
                        .locator("h2 a")
                        .get_attribute(
                            "href"
                        )
                    )

                    if link:

                        await browser.close()

                        return (
                            "https://www.amazon.in"
                            + link
                        )

            except Exception:
                pass

        await browser.close()

        return None