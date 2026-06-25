from app.services.history_service import (

    save_price,

    get_lowest_price

)

save_price(

    "Apple iPhone 15",

    "Flipkart",

    54900,

    "test"

)

print(

    get_lowest_price(

        "Apple iPhone 15"

    )

)