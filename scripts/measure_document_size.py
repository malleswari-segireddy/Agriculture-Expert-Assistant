from pathlib import Path

for file in Path("data/processed").glob("*.txt"):
    text = file.read_text(encoding="utf-8")

    print(
        file.name,
        len(text),
        "characters"
    )