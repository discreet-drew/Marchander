from app.services.history_service import *

save_price(

    "Apple iPhone 15",

    "Flipkart",

    54900,

    "test"

)

save_price(

    "Apple iPhone 15",

    "Amazon",

    55900,

    "test"

)

save_price(

    "Apple iPhone 15",

    "Flipkart",

    53900,

    "test"

)

print()

print("History")

print(get_price_history("iphone 15"))

print()

print("Lowest")

print(get_lowest_price("iphone 15"))

print()

print("Highest")

print(get_highest_price("iphone 15"))

print()

print("Average")

print(get_average_price("iphone 15"))

print()

print("Latest")

print(get_latest_price("iphone 15"))

print()

print("Analytics")

print(

    get_product_analytics(

        "iphone 15"

    )

)