import pickle
import numpy as np
import faiss
from pathlib import Path

EMBEDDING_DIR = Path("data/embeddings")
VECTOR_DIR = Path("vector_store")

VECTOR_DIR.mkdir(exist_ok=True)

all_chunks = []
all_embeddings = []

for file in EMBEDDING_DIR.glob("*.pkl"):

    with open(file, "rb") as f:
        data = pickle.load(f)

    all_chunks.extend(data["chunks"])
    all_embeddings.extend(data["embeddings"])

embeddings_array = np.array(
    all_embeddings,
    dtype="float32"
)

dimension = embeddings_array.shape[1]

index = faiss.IndexFlatL2(dimension)

index.add(embeddings_array)

faiss.write_index(
    index,
    str(VECTOR_DIR / "agriculture.index")
)

with open(
    VECTOR_DIR / "chunks.pkl",
    "wb"
) as f:
    pickle.dump(all_chunks, f)

print(
    f"Indexed {len(all_chunks)} chunks"
)
