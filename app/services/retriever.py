import faiss
import pickle

from app.services.embedding import generate_embeddings


index = faiss.read_index(
    "vector_store/agriculture.index"
)

with open(
    "vector_store/chunks.pkl",
    "rb"
) as f:
    chunks = pickle.load(f)


def retrieve_context(
    query,
    top_k=5
):

    query_embedding = generate_embeddings(
        [query]
    )

    distances, indices = index.search(
        query_embedding.astype("float32"),
        top_k
    )

    results = []

    for idx in indices[0]:
        results.append(
            chunks[idx]
        )

    return results
