# frontend/app.py

import streamlit as st
from components.sidebar import render_sidebar
from pages.landing import render_landing
from pages.project_view import render_project_view

st.set_page_config(layout="wide")

render_sidebar()

if "selected_project" not in st.session_state:
    render_landing()
else:
    render_project_view()
