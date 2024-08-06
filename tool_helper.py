from langchain_community.tools import WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper, GoogleSerperAPIWrapper
from langchain_core.tools import StructuredTool


def get_wikipedia_tool():
    api_wrapper = WikipediaAPIWrapper(top_k_results=1, doc_content_chars_max=100)
    return WikipediaQueryRun(api_wrapper=api_wrapper)


def get_search_tool():
    search = GoogleSerperAPIWrapper()
    return StructuredTool.from_function(
        name="Intermediate Answer",
        func=search.run,
        description="useful for when you need to ask with search"
    )
