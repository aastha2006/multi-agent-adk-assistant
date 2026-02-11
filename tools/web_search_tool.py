from google.adk.tools import Tool

def web_search_func(query: str) -> str:
    """Simulates a web search."""
    # In a real scenario, integrate with Google Search API or similar.
    # For this demo, returning a mock response.
    return f"Search results for '{query}': [Mock Result 1], [Mock Result 2]"

web_search_tool = Tool(
    name="web_search",
    description="Search the web for information",
    func=web_search_func
)
