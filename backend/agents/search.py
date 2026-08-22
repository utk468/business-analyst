import logging
import asyncio
# pyrefly: ignore [missing-import]
from duckduckgo_search import DDGS

logger = logging.getLogger("startup_consultant.search")


def _run_ddg_search(query: str, max_results: int) -> list:
    """
    Synchronous worker function to execute the DDG search.
    
    Args:
        query (str): The search query.
        max_results (int): Maximum number of results to return.
    
    Returns:
        list: List of search results.
    """
    with DDGS() as ddgs:
        return list(ddgs.text(query, max_results=max_results))


async def search_web(query: str, max_results: int = 5) -> str:
    """
    Asynchronously search the web for the given query using DuckDuckGo.
    
    Args:
        query (str): The search query.
        max_results (int): Maximum number of results to return.
    
    Returns:
        str: Formatted search results.

    "asyncio.to_thread" is used to run the blocking code in a separate thread to prevent the event loop from blocking

    result looks like : [{'title': 'title', 'href': 'url', 'body': 'snippet'}]
    """
    try:
        logger.info(f"Running web search for: '{query}'")

        results = await asyncio.to_thread(_run_ddg_search, query, max_results)

        if not results:
            return "No search results found."

        search_str = ""
        for i, r in enumerate(results):
            search_str += f"{i+1}. Title: {r.get('title')}\nURL: {r.get('href')}\nSnippet: {r.get('body')}\n\n"
        
        return search_str

    except Exception as e:
        logger.error(f"Search failed: {e}")
        return f"Search failed with error: {str(e)}"
