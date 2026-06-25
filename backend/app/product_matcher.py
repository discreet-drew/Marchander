from sentence_transformers import (
    SentenceTransformer,
    util
)

model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)

def match_products(
    title1,
    title2
):

    emb1 = model.encode(
        title1,
        convert_to_tensor=True
    )

    emb2 = model.encode(
        title2,
        convert_to_tensor=True
    )

    score = util.cos_sim(
        emb1,
        emb2
    ).item()

    return score