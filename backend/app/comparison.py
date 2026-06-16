def compare_prices(
    flipkart=None,
    amazon=None
):

    if (
        flipkart and
        flipkart.get("price")
    ):

        return {

            "flipkart": flipkart,

            "amazon": amazon,

            "best_store":
            "Flipkart",

            "lowest_price":
            flipkart["price"]
        }

    if (
        amazon and
        amazon.get("price")
    ):

        return {

            "flipkart": flipkart,

            "amazon": amazon,

            "best_store":
            "Amazon",

            "lowest_price":
            amazon["price"]
        }

    return {

        "flipkart": flipkart,

        "amazon": amazon,

        "best_store":
        "Unavailable",

        "lowest_price":
        None
    }