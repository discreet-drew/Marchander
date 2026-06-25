from app.product_matcher import (
    match_products
)

score = match_products(

    "Apple iPhone 15 Black 128GB",

    "Apple iPhone 15 128 GB Midnight"

)

print(score)