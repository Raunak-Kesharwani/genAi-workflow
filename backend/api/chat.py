# backend/api/chat.py

from fastapi import APIRouter, HTTPException
from shared.schemas import ChatRequest, ChatResponse
from backend.agents.agent_factory import build_agent

router = APIRouter()


@router.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):
    try:
        agent = build_agent(
            project_id=request.project_id,
            api_key=request.api_key
        )

        result = agent.invoke(
            {
                "messages": [
                    {"role": "user", "content": request.message}
                ]
            }
        )

        return ChatResponse(
            structured_response=result["structured_response"].model_dump()
        )

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
