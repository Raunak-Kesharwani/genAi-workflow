# backend/agents/response_schemas.py

from pydantic import BaseModel
from typing import Optional


class WeatherResponse(BaseModel):
    """
    Structured response for Weather Agent.
    """
    punny_response: str
    weather_conditions: Optional[str] = None
