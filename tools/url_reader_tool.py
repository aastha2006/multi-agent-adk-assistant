from google.adk.tools import Tool
import requests

def url_reader_func(url: str) -> str:
    """Reads content from a URL."""
    try:
        response = requests.get(url, timeout=10)
        return response.text[:2000] # Return first 2000 chars
    except Exception as e:
        return f"Error reading URL: {str(e)}"

url_reader_tool = Tool(
    name="url_reader",
    description="Read content from a URL",
    func=url_reader_func
)
