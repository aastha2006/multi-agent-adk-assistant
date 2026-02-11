from google.adk.agent import Agent
from llm.gemini_config import DEFAULT_MODEL

writer_agent = Agent(
    name="WriterAgent",
    model=DEFAULT_MODEL,
    instruction="""
You generate final responses.

Responsibilities:
- Create clear, user-friendly output based on analysis.
- Format the response properly (e.g., using Markdown).
- Ensure high-quality writing.
"""
)
