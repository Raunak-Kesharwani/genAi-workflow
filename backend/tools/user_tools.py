# backend/tools/user_tools.py

import requests
from langchain.tools import tool


@tool
def get_user_location() -> str:
    """
    Get user's city using IP-based lookup.
    """
    try:
        response = requests.get("https://ipapi.co/json/", timeout=5)
        data = response.json()
        return data.get("city") or "Unknown"
    except Exception:
        return "Unknown"
