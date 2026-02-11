import google.generativeai as genai
from typing import List, Optional, Any
import os
from dotenv import load_dotenv
from .tools import Tool

# Load environment variables
load_dotenv()

# Configure genai once
api_key = os.getenv("GEMINI_API_KEY") or os.getenv("GOOGLE_API_KEY")
if api_key:
    genai.configure(api_key=api_key)

class Agent:
    def __init__(self, name: str, model: str, instruction: str, tools: List[Tool] = None, sub_agents: List['Agent'] = None):
        self.name = name
        self.model_name = model
        self.instruction = instruction
        self.tools = tools or []
        self.sub_agents = sub_agents or []
        
        # Initialize Gemini model
        # Convert tools to genai compatible format if needed, but for now passing as functions
        # Note: In a real library this would map Tools to FunctionDeclarations
        self.model = genai.GenerativeModel(
            model_name=model,
            system_instruction=instruction,
            tools=[t.func for t in self.tools] if self.tools else None
        )

    def generate_response(self, history, message):
        chat = self.model.start_chat(history=history)
        response = chat.send_message(message)
        return response.text
