# backend/tools/user_tools.py

import requests
from dataclasses import dataclass
from langchain.tools import tool, ToolRuntime


@dataclass
class Context:
    user_id: str


@tool
def get_user_location(runtime: ToolRuntime[Context]) -> str:
    """
    Get user's city using IP-based lookup.
    """
    try:
        response = requests.get("https://ipapi.co/json/", timeout=5)
        data = response.json()
        city = data.get("city")
        return city or "Unknown"
    except Exception:
        return "Unknown"
