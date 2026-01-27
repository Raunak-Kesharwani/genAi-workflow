# frontend/services/api_client.py

import requests
from frontend.utils.config import BACKEND_URL

def send_chat_message(
    *,
    project_id: str,
    message: str,
    api_key: str
):
    payload = {
        "project_id": project_id,
        "message": message,
        "api_key": api_key
    }

    response = requests.post(
        f"{BACKEND_URL}/chat",
        json=payload,
        timeout=30
    )

    response.raise_for_status()
    return response.json()
