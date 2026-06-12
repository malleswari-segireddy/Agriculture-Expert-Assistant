from pathlib import Path
import json

from app.services.chunking import chunk_text

INPUT_DIR = Path("data/processed")
OUTPUT_DIR = Path("data/chunks")

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

for file in INPUT_DIR.glob("*.txt"):
    text = file.read_text(encoding="utf-8")

    chunks = chunk_text(text)

    output_file = OUTPUT_DIR / f"{file.stem}.json"

    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(chunks, f, ensure_ascii=False, indent=2)

    print(
        f"{file.name} -> {len(chunks)} chunks"
    )
