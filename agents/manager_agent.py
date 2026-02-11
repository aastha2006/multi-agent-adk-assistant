from google.adk.agent import Agent
from agents.research_agent import research_agent
from agents.analyst_agent import analyst_agent
from agents.writer_agent import writer_agent
from llm.gemini_config import DEFAULT_MODEL
from memory.vector_store import vector_store

manager_agent = Agent(
    name="ManagerAgent",
    model=DEFAULT_MODEL,
    instruction="""
You are responsible for orchestrating a multi-agent workflow.

Steps:
1. Delegate research tasks to ResearchAgent to gather information.
2. Delegate analysis tasks to AnalystAgent to process the findings.
3. Delegate response generation to WriterAgent to create the final answer.

Use memory context when available (retrieve_memory is handled by the system or you can request it).
Ensure the final response is comprehensive and addresses the user's request.
""",
    sub_agents=[
        research_agent,
        analyst_agent,
        writer_agent
    ]
)
