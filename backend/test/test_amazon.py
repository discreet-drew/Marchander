# test_amazon.py

from app.scrapers.Electronics.amazon import (
    scrape_amazon
)

url = "https://www.amazon.in/Apple-iPhone-17e-256-GB/dp/B0GQVL6STN"

result = scrape_amazon(
    url
)

print(result)