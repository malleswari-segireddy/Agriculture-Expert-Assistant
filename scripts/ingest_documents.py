from pathlib import Path
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))
from app.services.pdf_loader import extract_text_from_pdf


RAW_DATA_DIR = Path("data/raw")
PROCESSED_DIR = Path("data/processed")

PROCESSED_DIR.mkdir(parents=True, exist_ok=True)


for pdf_file in RAW_DATA_DIR.glob("*.pdf"):
    print(f"Processing: {pdf_file.name}")

    text = extract_text_from_pdf(pdf_file)

    output_file = PROCESSED_DIR / f"{pdf_file.stem}.txt"

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(text)

    print(f"Saved: {output_file}")
