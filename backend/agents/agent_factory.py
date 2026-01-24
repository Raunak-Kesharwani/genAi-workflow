# backend/agents/agent_factory.py

from langchain.agents import create_agent
from langchain.agents.structured_output import ToolStrategy
from langgraph.checkpoint.memory import InMemorySaver

from backend.projects.registry import get_project
from backend.core.llm import get_gemini_model


def build_agent(
    *,
    project_id: str,
    api_key: str,
    thread_id: str,
    context_schema=None
):
    """
    Build an agent dynamically based on project configuration.
    """

    # 1️⃣ Load project configuration
    project = get_project(project_id)

    # 2️⃣ Create LLM
    model = get_gemini_model(api_key=api_key)

    # 3️⃣ Memory / checkpointing
    checkpointer = InMemorySaver()

    # 4️⃣ Build agent
    agent = create_agent(
        model=model,
        system_prompt=project.system_prompt,
        tools=project.tools,
        context_schema=context_schema,
        response_format=ToolStrategy(project.response_schema),
        checkpointer=checkpointer
    )

    # 5️⃣ Runtime config (thread-based memory)
    config = {
        "configurable": {
            "thread_id": thread_id
        }
    }

    return agent, config
