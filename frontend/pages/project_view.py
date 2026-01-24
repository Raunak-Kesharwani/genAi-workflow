# frontend/pages/project_view.py

import streamlit as st
from services.api_client import send_chat_message


def render_project_view():
    project_id = st.session_state.selected_project
    st.title(f"🗂 Project: {project_id}")

    if "messages" not in st.session_state:
        st.session_state.messages = []

    for msg in st.session_state.messages:
        st.chat_message(msg["role"]).write(msg["content"])

    user_input = st.chat_input("Type your message")

    if user_input:
        st.session_state.messages.append(
            {"role": "user", "content": user_input}
        )

        response = send_chat_message(
            project_id=project_id,
            user_id="1",
            message=user_input,
            api_key=st.session_state.api_key
        )

        assistant_reply = response["structured_response"]

        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": assistant_reply
            }
        )

        st.rerun()
