from dotenv import load_dotenv

load_dotenv()

from typing import TypedDict

from langgraph.graph import (
    StateGraph,
    END
)

from langchain_groq import ChatGroq

from src.retriever import hybrid_retriever

from src.websearch import web_search
from src.prompts import SYSTEM_PROMPT


# LLM

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0,
    streaming=True
)


# SENTIMENT WORDS

negative_words = [

    "bad",

    "angry",

    "worst",

    "frustrated",

    "late",

    "terrible",

    "damaged",

    "refund problem",

    "not working"
]


# GRAPH STATE

class GraphState(TypedDict):

    question: str

    context: str

    answer: str

    history: list


# RAG SEARCH

def rag_search(query):

    docs = hybrid_retriever.invoke(
        query
    )

    return "\n\n".join(
        [d.page_content for d in docs]
    )


# ROUTER

def router(state):

    question = state[
        "question"
    ]

    if "latest" in question.lower():

        return "web"

    return "rag"


# RAG NODE

def rag_node(state):

    result = rag_search(
        state["question"]
    )

    return {
        "context": result
    }


# WEB NODE

def web_node(state):

    result = web_search(
        state["question"]
    )

    return {
        "context": result
    }


# GENERATE RESPONSE

def generate(state):

    history = state.get(
        "history",
        []
    )

    question = state[
        "question"
    ]

    # SENTIMENT DETECTION

    sentiment = "normal"

    for word in negative_words:

        if word in question.lower():

            sentiment = "angry"

    # PROMPT

    prompt = f"""

    {SYSTEM_PROMPT}

    User Sentiment:
    {sentiment}

    If user sentiment is angry:
    - apologize politely
    - sound empathetic
    - try calming the user

    Previous Conversation:
    {history}

    Context:
    {state['context']}

    User Question:
    {state['question']}

    Give a professional ecommerce support response.
    """

    response = llm.invoke(
        prompt
    )

    return {
        "answer":
        response.content
    }


# GRAPH

builder = StateGraph(
    GraphState
)

builder.add_node(
    "rag",
    rag_node
)

builder.add_node(
    "web",
    web_node
)

builder.add_node(
    "generate",
    generate
)

builder.set_conditional_entry_point(
    router,
    {
        "rag": "rag",
        "web": "web"
    }
)

builder.add_edge(
    "rag",
    "generate"
)

builder.add_edge(
    "web",
    "generate"
)

builder.add_edge(
    "generate",
    END
)

graph = builder.compile()