from app.scrapers.Electronics.flipkart import scrape_flipkart #type: ignore

url = (
    "https://www.flipkart.com/apple-iphone-15-black-128-gb/p/itm6ac6485515ae4"
)

result = scrape_flipkart(url)

print(result)