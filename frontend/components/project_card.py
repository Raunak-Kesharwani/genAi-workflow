# frontend/components/project_card.py

import streamlit as st


def project_card(project, on_click):
    with st.container(border=True):
        st.subheader(project["name"])
        st.write(project["description"])
        if st.button("Open", key=project["project_id"]):
            on_click(project["project_id"])
