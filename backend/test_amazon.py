from app.scrapers.amazon import scrape_amazon

url = (
    "https://www.amazon.in/dp/B0CHX1W1XY"
)

result = scrape_amazon(url)

print(result)