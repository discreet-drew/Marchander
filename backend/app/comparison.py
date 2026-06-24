def compare_prices(
    flipkart,
    amazon
):

    valid = []

    if (
        flipkart and
        flipkart.get("price")
    ):

        flipkart_price = int(
            str(
                flipkart["price"]
            ).replace(",", "")
        )

        valid.append(
            (
                "Flipkart",
                flipkart_price
            )
        )

    if (
        amazon and
        amazon.get("price")
    ):

        amazon_price = int(
            str(
                amazon["price"]
            ).replace(",", "")
        )

        valid.append(
            (
                "Amazon",
                amazon_price
            )
        )

    if not valid:

        return {

            "flipkart": flipkart,

            "amazon": amazon,

            "best_store":
            "Unavailable",

            "lowest_price":
            None,

            "price_difference":
            0
        }

    best_store, lowest_price = min(
        valid,
        key=lambda x: x[1]
    )

    highest_price = max(
        p[1]
        for p in valid
    )

    savings = (
        highest_price
        - lowest_price
    )

    return {

        "flipkart": flipkart,

        "amazon": amazon,

        "best_store":
        best_store,

        "lowest_price":
        lowest_price,

        "price_difference":
        savings
    }