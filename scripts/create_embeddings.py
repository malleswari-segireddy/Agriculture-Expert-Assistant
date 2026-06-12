import json
import pickle
from pathlib import Path

from app.services.embedding import generate_embeddings

CHUNK_DIR = Path("data/chunks")
OUTPUT_DIR = Path("data/embeddings")

OUTPUT_DIR.mkdir(
    parents=True,
    exist_ok=True
)

for file in CHUNK_DIR.glob("*.json"):

    with open(file, "r", encoding="utf-8") as f:
        chunks = json.load(f)

    embeddings = generate_embeddings(chunks)

    output_file = OUTPUT_DIR / f"{file.stem}.pkl"

    with open(output_file, "wb") as f:
        pickle.dump(
            {
                "chunks": chunks,
                "embeddings": embeddings
            },
            f
        )

    print(
        f"{file.name}: {len(chunks)} embeddings created"
    )
