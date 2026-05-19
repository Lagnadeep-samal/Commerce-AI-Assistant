# Technical Documentation

# Architecture

Frontend:
- HTML
- CSS
- JavaScript

Backend:
- Flask API

AI Layer:
- LangGraph
- LangChain
- Groq LLM

Retrieval:
- FAISS Vector Store
- BM25 Retriever
- Ensemble Retriever

---

# Workflow

User Query
↓
LangGraph Router
↓
RAG or Web Search
↓
LLM Generation
↓
Streaming Response

---

# Components

## Retriever

Hybrid retrieval combines:
- Semantic Search
- Keyword Search

using EnsembleRetriever.

---

## Router

Determines whether:
- query requires latest info
OR
- internal knowledge retrieval

---

## Streaming

Frontend uses:
- fetch()
- ReadableStream
- TextDecoder

to stream tokens.

---

# Embeddings

Model:
BAAI/bge-small-en-v1.5

Stored in:
FAISS local vector database

---

# Failure Handling

Implemented:
- Empty input checks
- API validation
- Missing payment fields
- Limited history size

Not Implemented:
- Rate limiting
- Retry logic
- Distributed persistence

---

# Limitations

- Local FAISS database
- No authentication
- Simulated payment pipeline
- No production monitoring
- No multi-user memory

---

# Future Improvements

- PostgreSQL integration
- Redis caching
- Cloud vector DB
- JWT Authentication
- Admin analytics panel
- Voice assistant
- Real payment gateway