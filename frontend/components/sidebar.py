# frontend/components/sidebar.py

import streamlit as st


def render_sidebar():
    st.sidebar.title("⚙️ Settings")

    if "api_key" not in st.session_state:
        st.session_state.api_key = ""

    st.sidebar.subheader("Gemini API Key")
    st.session_state.api_key = st.sidebar.text_input(
        "Enter API Key",
        type="password",
        value=st.session_state.api_key
    )

    st.sidebar.subheader("Appearance")
    st.session_state.theme = st.sidebar.selectbox(
        "Theme",
        ["Light", "Dark"]
    )

    st.session_state.font = st.sidebar.selectbox(
        "Font",
        ["Default", "Monospace"]
    )
