from fastapi import FastAPI, HTTPException
from google.adk.runner import Runner
from google.adk.session import Session
from agents.manager_agent import manager_agent
from api.schemas import ChatRequest, ChatResponse
import uuid

app = FastAPI(title="Multi-Agent ADK Assistant")

# Initialize Runner
runner = Runner(
    agent=manager_agent,
    app_name="multi-agent-adk-assistant"
)

# In-memory session storage (Production would use Redis/Database)
sessions = {}

@app.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):
    try:
        session_id = request.session_id
        session = None

        if session_id and session_id in sessions:
            session = sessions[session_id]
        else:
            session = Session()
            session_id = str(uuid.uuid4())
            sessions[session_id] = session

        # Execute agent workflow
        result = runner.run(
            session=session,
            input=request.message
        )

        return ChatResponse(
            response=result.output,
            session_id=session_id
        )

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.get("/")
def root():
    return {
        "message": "Welcome to the Multi-Agent ADK Assistant API",
        "endpoints": {
            "chat": "POST /chat",
            "docs": "/docs"
        }
    }
