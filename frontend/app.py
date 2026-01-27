# frontend/app.py
import sys
from pathlib import Path

# Add project root to Python path
ROOT_DIR = Path(__file__).resolve().parent.parent
if str(ROOT_DIR) not in sys.path:
    sys.path.append(str(ROOT_DIR))


import streamlit as st
from frontend.components.sidebar import render_sidebar
from frontend.pages.landing import render_landing
from frontend.pages.project_view import render_project_view

st.set_page_config(
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items=None
)

render_sidebar()

if "selected_project" not in st.session_state:
    render_landing()
else:
    render_project_view()
