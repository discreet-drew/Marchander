from sentence_transformers import SentenceTransformer
from sentence_transformers import util

from .products import POPULAR_PRODUCTS

model = SentenceTransformer("all-MiniLM-L6-v2")

embeddings = model.encode(
    POPULAR_PRODUCTS,
    convert_to_tensor=True
)


def suggest_products(query):

    if not query:
        return []

    query_embedding = model.encode(
        query,
        convert_to_tensor=True
    )

    scores = util.cos_sim(
        query_embedding,
        embeddings
    )[0]

    ranked = sorted(
        zip(
            POPULAR_PRODUCTS,
            scores.tolist()
        ),
        key=lambda x: x[1],
        reverse=True
    )

    recommendations = []

    for product, score in ranked[:5]:

        recommendations.append(
            {
                "product": product,
                "score": round(score, 3)
            }
        )

    return recommendations