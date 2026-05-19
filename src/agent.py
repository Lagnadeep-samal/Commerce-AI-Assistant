from src.retriever import hybrid_retriever

from src.websearch import web_search


def decide_source(query):

    query = query.lower()

    keywords = [
        "latest",
        "today",
        "news",
        "recent"
    ]

    for k in keywords:

        if k in query:
            return "web"

    return "rag"


def agent_search(query):

    route = decide_source(query)

    if route == "web":

        return web_search(query)

    docs = hybrid_retriever.invoke(query)

    return "\n\n".join(
        [d.page_content for d in docs]
    )