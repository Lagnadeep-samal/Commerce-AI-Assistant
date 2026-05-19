from langchain_huggingface import (
    HuggingFaceEmbeddings
)

from langchain_community.vectorstores import FAISS

from langchain_community.retrievers import (
    BM25Retriever
)

from langchain_classic.retrievers import (
    EnsembleRetriever
)

embedding = HuggingFaceEmbeddings(
    model_name="BAAI/bge-small-en-v1.5"
)


db = FAISS.load_local(
    "vectordb",
    embedding,
    allow_dangerous_deserialization=True
)

vector_retriever = db.as_retriever(
    search_type="mmr",
    search_kwargs={
        "k": 5,
        "fetch_k": 20,
        "lambda_mult": 0.7
    }
)


docs = list(db.docstore._dict.values())

bm25_retriever = BM25Retriever.from_documents(
    docs
)

bm25_retriever.k = 5

hybrid_retriever = EnsembleRetriever(
    retrievers=[
        bm25_retriever,
        vector_retriever
    ],
    weights=[0.4, 0.6]
)