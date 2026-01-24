# frontend/pages/landing.py

import streamlit as st
import requests
from components.project_card import project_card

BACKEND_URL = "http://localhost:8000/api"


def set_project(project_id: str):
    st.session_state.selected_project = project_id


def render_landing():
    st.title("🧪 AI Project Lab")
    st.write("Select a project to explore")

    response = requests.get(f"{BACKEND_URL}/projects")
    projects = response.json()

    cols = st.columns(2)

    for idx, project in enumerate(projects):
        with cols[idx % 2]:
            project_card(
                project,
                on_click=lambda pid=project["project_id"]: set_project(pid)
            )
