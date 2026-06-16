from app.services.retriever import retrieve_context
from app.services.llm_service import generate_answer

question = input("What fertilizer is recommended for paddy?")

chunks = retrieve_context(
    question,
    top_k=5
)

context = "\n\n".join(chunks)

answer = generate_answer(
    question,
    context
)

print("\nAnswer:")
print(answer)
