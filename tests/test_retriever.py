
from pathlib import Path
import sys


sys.path.append(str(Path(__file__).resolve().parent.parent))
from app.services.retriever import retrieve_context

results = retrieve_context(
    "What fertilizer is recommended for paddy?" # Replace with your query
)

for i, result in enumerate(results):
    print(f"\n--- Result {i+1} ---")
    print(result[:500])
