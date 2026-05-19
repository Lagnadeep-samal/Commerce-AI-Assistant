# Product Document

# Product Name

Commerce AI Assistant

---

# What We Built

Commerce AI Assistant is an AI-powered ecommerce customer support platform designed to automate customer support operations.

The system combines:
- Retrieval-Augmented Generation (RAG)
- Web Search
- Streaming AI responses
- Ecommerce workflows

into a unified intelligent support experience.

---

# Target Users

- Ecommerce platforms
- Online stores
- Customer support teams
- D2C brands

---

# Core Problems Solved

1. Slow customer support
2. Repetitive queries
3. Poor chatbot experiences
4. Non-contextual responses
5. Lack of real-time information

---

# Key Features

- Intelligent support chatbot
- Hybrid retrieval
- Latest web information retrieval
- Streaming responses
- Product cards
- Order tracking interface
- Payment UI simulation
- Suggested replies
- Analytics dashboard

---

# Key Product Decisions

## Why RAG?

RAG allows the chatbot to answer using company-specific knowledge instead of hallucinating.

## Why Hybrid Retrieval?

Combining BM25 + Vector Search improves semantic understanding and keyword matching.

## Why Streaming Responses?

Streaming improves user experience and mimics modern conversational AI systems.

## Why LangGraph?

LangGraph enables routing between:
- RAG workflows
- Web Search workflows

---

# Scope

Included:
- AI support assistant
- RAG pipeline
- Streaming frontend
- Dynamic UI

Not Included:
- Real payment processing
- Authentication
- Production deployment pipeline
- Database persistence

---

# Tradeoffs

We prioritized:
- Faster prototyping
- Better UX
- Simpler architecture

instead of:
- Enterprise-grade scalability
- Complex orchestration