def compare_prices(
    flipkart=None,
    amazon=None
):

    valid_prices = []

    if (
        flipkart and
        flipkart.get("price")
    ):
        valid_prices.append(
            (
                "Flipkart",
                int(
                    str(
                        flipkart["price"]
                    ).replace(",", "")
                )
            )
        )

    if (
        amazon and
        amazon.get("price")
    ):
        valid_prices.append(
            (
                "Amazon",
                int(
                    str(
                        amazon["price"]
                    ).replace(",", "")
                )
            )
        )

    if not valid_prices:

        return {
            "message":
            "Product unavailable on all stores"
        }

    best_store, lowest_price = min(
        valid_prices,
        key=lambda x: x[1]
    )

    return {

        "flipkart": flipkart,

        "amazon": amazon,

        "lowest_price":
        lowest_price,

        "best_store":
        best_store
    }