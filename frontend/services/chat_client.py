# frontend/services/chat_client.py

from backend.service import chat_service


def send_chat_message(project_id: str, message: str, api_key: str):
    return chat_service(
        project_id=project_id,
        message=message,
        api_key=api_key
    )
