from langchain_core.tools import Tool

from langchain_community.tools import (
    DuckDuckGoSearchRun
)

search = DuckDuckGoSearchRun()


def web_search(query):

    return search.run(query)


web_tool = Tool(
    name="DuckDuckGo Search",
    func=web_search,
    description="Useful for latest ecommerce information"
)