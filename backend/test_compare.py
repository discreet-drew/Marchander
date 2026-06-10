from app.comparison import (
    compare_prices
)

flipkart = {

    "store":"Flipkart",

    "price":59900
}

amazon = {

    "store":"Amazon",

    "price":64900
}

print(

    compare_prices(
        flipkart,
        amazon
    )
)