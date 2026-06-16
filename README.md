# Agriculture Expert Assistant (RAG-Based AI System)

## Overview

Agriculture Expert Assistant is a Retrieval-Augmented Generation (RAG) application that helps users get accurate answers related to agriculture, including:

* Crop cultivation practices
* Fertilizer recommendations
* Pest management
* Irrigation methods
* Government agricultural schemes
* Agricultural research and best practices

The system retrieves relevant information from agricultural documents and uses Google's Gemini model to generate context-aware answers.

---

# Architecture

```text
Agriculture PDFs
        ↓
PDF Extraction
        ↓
Text Files
        ↓
Chunking
        ↓
Embeddings
        ↓
FAISS Vector Store
        ↓
Retriever
        ↓
Gemini LLM
        ↓
Generated Answer
```

---

# Project Structure

```text
agriculture-expert-assistant/
│
├── app/
│   ├── api/
│   │   └── routes.py
│   │
│   ├── services/
│   │   ├── pdf_loader.py
│   │   ├── chunking.py
│   │   ├── embedding.py
│   │   ├── vector_store.py
│   │   ├── retriever.py
│   │   └── llm_service.py
│   │
│   ├── models/
│   │   └── schemas.py
│   │
│   └── main.py
│
├── data/
│   ├── raw/
│   ├── processed/
│   ├── chunks/
│   └── embeddings/
│
├── vector_store/
│
├── scripts/
│   ├── ingest_documents.py
│   ├── create_chunks.py
│   ├── create_embeddings.py
│   ├── build_faiss_index.py
│   └── test_rag.py
│
├── tests/
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```

---

# Prerequisites

* Python 3.10+
* Virtual Environment
* Google Gemini API Key

---

# Setup Instructions

## 1. Clone Repository

```bash
git clone <repository-url>
cd agriculture-expert-assistant
```

---

## 2. Create Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux/Mac

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install pypdf
pip install sentence-transformers
pip install faiss-cpu
pip install google-generativeai
pip install python-dotenv
pip install numpy
```

Or:

```bash
pip install -r requirements.txt
```

---

# Step 1: Add Agriculture Documents

Place all PDF documents inside:

```text
data/raw/
```

Example:

```text
data/raw/
├── paddy_cultivation.pdf
├── cotton_cultivation.pdf
├── fertilizer_guide.pdf
└── government_schemes.pdf
```

---

# Step 2: Extract Text From PDFs

Run:

```bash
python -m scripts.ingest_documents
```

Output:

```text
data/processed/
├── paddy_cultivation.txt
├── cotton_cultivation.txt
├── fertilizer_guide.txt
└── government_schemes.txt
```

---

# Step 3: Create Chunks

Run:

```bash
python -m scripts.create_chunks
```

Output:

```text
data/chunks/
├── paddy_cultivation.json
├── cotton_cultivation.json
├── fertilizer_guide.json
└── government_schemes.json
```

Each JSON file contains chunked text segments.

---

# Step 4: Generate Embeddings

Run:

```bash
python -m scripts.create_embeddings
```

Output:

```text
data/embeddings/
├── paddy_cultivation.pkl
├── cotton_cultivation.pkl
├── fertilizer_guide.pkl
└── government_schemes.pkl
```

Each file contains:

* Chunks
* Vector Embeddings

Generated using:

```text
all-MiniLM-L6-v2
```

Sentence Transformer model.

---

# Step 5: Build FAISS Index

Run:

```bash
python -m scripts.build_faiss_index
```

Output:

```text
vector_store/
├── agriculture.index
└── chunks.pkl
```

This creates the semantic search index.

---

# Step 6: Test Retriever

Example:

```python
from app.services.retriever import retrieve_context

results = retrieve_context(
    "Best fertilizer for paddy",
    top_k=5
)

for result in results:
    print(result)
```

Retriever returns the most relevant chunks from the knowledge base.

---

# Step 7: Create Gemini API Key

Visit:

https://aistudio.google.com/apikey

Create a new API key.

---

# Step 8: Configure Environment Variables

Create `.env`

```env
GEMINI_API_KEY=YOUR_API_KEY
```

Example:

```env
GEMINI_API_KEY=AIzaSyXXXXXXXXXXXXXXXXXXXXX
```

---

# Step 9: Gemini Integration

Install:

```bash
pip install google-generativeai
pip install python-dotenv
```

Test Gemini:

```python
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

response = model.generate_content(
    "Explain paddy cultivation."
)

print(response.text)
```

Run:

```bash
python test_gemini.py
```

Expected:

```text
Paddy cultivation involves...
```

---

# Step 10: Run Complete RAG Flow

Run:

```bash
python -m scripts.test_rag
```

Example:

```text
Ask Question:
What fertilizer is recommended for paddy?
```

Workflow:

```text
Question
 ↓
Embedding
 ↓
FAISS Retrieval
 ↓
Relevant Chunks
 ↓
Gemini
 ↓
Generated Answer
```

Output:

```text
According to the cultivation guide,
nitrogen fertilizer is recommended during
the vegetative stage...
```

---

# Current Features

✅ PDF Document Ingestion

✅ Text Extraction

✅ Chunking

✅ Embedding Generation

✅ Semantic Search

✅ FAISS Vector Database

✅ Context Retrieval

✅ Gemini Integration

✅ End-to-End RAG Pipeline

---

# Future Enhancements

* FastAPI REST APIs
* Streamlit Chat Interface
* Source Citations
* Metadata Filtering
* Crop-Based Search
* Multilingual Support
* Voice-Based Queries
* Docker Deployment
* CI/CD Integration

---

# Tech Stack

* Python
* Sentence Transformers
* FAISS
* Google Gemini
* NumPy
* PyPDF
* FastAPI (Upcoming)
* Docker (Upcoming)

---

# Learning Outcomes

This project demonstrates:

* Retrieval-Augmented Generation (RAG)
* Semantic Search
* Vector Embeddings
* Vector Databases
* Information Retrieval
* LLM Integration
* End-to-End AI Application Development
