import os

from dotenv import load_dotenv
from langchain.tools import tool
from tavily import TavilyClient

load_dotenv()

TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")


@tool(parse_docstring=True)
def search_web(query: str) -> str:
    """Search the internet for up-to-date information about a topic.

    Args:
        query: The search query, e.g. a topic, question, or name to look up.

    Returns:
        A short answer summarizing the findings, followed by a list of
        source titles and URLs. Preserve the source URLs when passing this
        information along (e.g. when posting it elsewhere).
    """
    if not TAVILY_API_KEY:
        raise RuntimeError("TAVILY_API_KEY is not set in the environment")

    client = TavilyClient(api_key=TAVILY_API_KEY)
    response = client.search(query, max_results=5, include_answer=True)

    answer = response.get("answer", "")
    sources = "\n".join(
        f"- {item['title']}: {item['url']}" for item in response.get("results", [])
    )
    return f"Answer: {answer}\n\nSources:\n{sources}"
