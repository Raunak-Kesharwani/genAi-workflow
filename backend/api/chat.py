# backend/api/chat.py

from fastapi import APIRouter, HTTPException
from shared.schemas import ChatRequest, ChatResponse

from backend.agents.agent_factory import build_agent
from backend.projects.registry import get_project

from dataclasses import dataclass


router = APIRouter()


@dataclass
class Context:
    user_id: str


@router.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):
    try:
        # 1️⃣ Validate project exists
        project = get_project(request.project_id)

        # 2️⃣ Build thread_id (per user + per project)
        thread_id = f"{request.user_id}_{request.project_id}"

        # 3️⃣ Build agent dynamically
        agent, config = build_agent(
            project_id=request.project_id,
            api_key=request.api_key,
            thread_id=thread_id,
            context_schema=Context
        )

        # 4️⃣ Invoke agent
        result = agent.invoke(
            {
                "messages": [
                    {"role": "user", "content": request.message}
                ]
            },
            config=config,
            context=Context(user_id=request.user_id)
        )

        # 5️⃣ Return structured response only
        return ChatResponse(
    structured_response=result["structured_response"].model_dump()
    )

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
