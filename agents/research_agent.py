from google.adk.agent import Agent
from tools.web_search_tool import web_search_tool
from tools.url_reader_tool import url_reader_tool
from llm.gemini_config import DEFAULT_MODEL

research_agent = Agent(
    name="ResearchAgent",
    model=DEFAULT_MODEL,
    instruction="""
You are a research specialist.

Responsibilities:
- Search for information using the web_search tool.
- Gather facts from URLs using the url_reader tool.
- Provide structured research output with sources.
""",
    tools=[web_search_tool, url_reader_tool]
)
