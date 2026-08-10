from pathlib import Path
import streamlit as st

BASE_DIR = Path(__file__).resolve().parent

if "theme" not in st.session_state:
    st.session_state.theme = "dark"

def toggle_theme():
    st.session_state.theme = (
        "light" if st.session_state.theme == "dark" else "dark"
    )

def load_theme_css():
    css_file = (
        BASE_DIR / "light_style.css"
        if st.session_state.theme == "light"
        else BASE_DIR / "dark_style.css"
    )
    css = css_file.read_text(encoding="utf-8")
    st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)

load_theme_css()

theme_icon = "☀" if st.session_state.theme == "dark" else "☾"
st.button(
    theme_icon,
    key="theme_button",
    on_click=toggle_theme,
    help="Toggle light / dark mode",
)