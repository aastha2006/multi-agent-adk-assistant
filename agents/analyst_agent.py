from google.adk.agent import Agent
from llm.gemini_config import DEFAULT_MODEL

analyst_agent = Agent(
    name="AnalystAgent",
    model=DEFAULT_MODEL,
    instruction="""
You analyze research results.

Responsibilities:
- Extract insights from provided text.
- Identify key patterns and trends.
- Provide structured analysis notes.
"""
)
