import os

from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

model = genai.GenerativeModel(
    "gemini-2.5-flash"
)


def generate_answer(
    question,
    context
):

    prompt = f"""
You are an Agriculture Expert Assistant.

Answer ONLY using the provided context.

If the answer is not found in the context,
say:
"I could not find sufficient information in the knowledge base."

Context:
{context}

Question:
{question}
"""

    response = model.generate_content(
        prompt
    )

    return response.text
