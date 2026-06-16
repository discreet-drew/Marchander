from app.comparison import compare_prices

flipkart = None

amazon = {
    "price": 58999
}
print(
    compare_prices(
        flipkart,
        amazon
    )
)