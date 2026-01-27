# backend/service.py

from backend.agents.agent_factory import build_agent


def chat_service(project_id: str, message: str, api_key: str):
    agent = build_agent(
        project_id=project_id,
        api_key=api_key
    )

    result = agent.invoke(
        {
            "messages": [
                {"role": "user", "content": message}
            ]
        }
    )

    return result["structured_response"].model_dump()
