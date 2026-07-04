from app.ai.recommender import suggest_products

queries = [
    "iphone",
    "iphone 15",
    "samsung",
    "oneplus",
    "airpods",
    "watch"
]

for query in queries:

    print("=" * 50)
    print("Query:", query)

    recommendations = suggest_products(query)

    for product, score in recommendations:

        print(f"{product} -> {round(score, 4)}")