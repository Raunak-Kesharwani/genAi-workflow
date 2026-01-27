# frontend/pages/landing.py

import streamlit as st
from frontend.components.project_card import project_card
from backend.projects.registry import list_projects

def set_project(project_id: str):
    st.session_state.selected_project = project_id


def render_landing():
    st.title("🧪 AI Project Lab")
    st.write("Select a project to explore")

    
    projects = list_projects()

    cols = st.columns(2)

    for idx, project in enumerate(projects):
        with cols[idx % 2]:
            project_card(
                project,
                on_click=lambda pid=project["project_id"]: set_project(pid)
            )
