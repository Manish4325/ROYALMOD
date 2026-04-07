import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="ROYALMOD", layout="wide", initial_sidebar_state="collapsed")

# Hide Streamlit default UI for a clean experience
st.markdown("""
<style>
    #MainMenu {visibility: hidden;}
    header {visibility: hidden;}
    footer {visibility: hidden;}
    .stApp > div:first-child {padding-top: 0;}
    iframe {border: none;}
    .block-container {padding: 0 !important; max-width: 100% !important;}
</style>
""", unsafe_allow_html=True)

# Read and serve index.html
with open("index.html", "r", encoding="utf-8") as f:
    html_content = f.read()

components.html(html_content, height=800, scrolling=True)
