# shared/schemas.py

from pydantic import BaseModel
from typing import Any, Dict


class ChatRequest(BaseModel):
    project_id: str
    user_id: str
    message: str
    api_key: str | None = None


class ChatResponse(BaseModel):
    structured_response: Dict[str, Any]
