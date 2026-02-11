from .agent import Agent
from .session import Session

class RunnerResult:
    def __init__(self, output: str, full_history: list = None):
        self.output = output
        self.full_history = full_history

class Runner:
    def __init__(self, agent: Agent, app_name: str = "adk-app"):
        self.root_agent = agent
        self.app_name = app_name

    def run(self, session: Session, input: str) -> RunnerResult:
        # Simple Runner implementation: just call the root agent
        # In a real ADK, this handles complex routing
        
        # Retrieve history from session
        history = [] # simplify history conversion for now
        
        # If manager agent has sub_agents, we might need manual routing or let the LLM decide.
        # For simplicity in this emulator, we treat the manager as the primary responder 
        # who has the context of "I can delegate...". 
        # However, without actual function calling for delegation implemented in this mockup, 
        # the manager will just simulate the response or use the tools provided.
        
        # Since the user requested explicit orchestration in instruction, 
        # the model should output text that *looks* like delegation or final answer.
        # To truly orchestrate, we'd need to parse the response or give it tools to call agents.
        # For this MVP ensuring import correctness:
        
        try:
            response_text = self.root_agent.generate_response(history=history, message=input)
            
            # Update session
            session.add_context("user", input)
            session.add_context("model", response_text)
            
            return RunnerResult(output=response_text)
        except Exception as e:
            return RunnerResult(output=f"Agent Error: {str(e)}")
