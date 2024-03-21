import streamlit as st

st.set_page_config(
    page_title="BI",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded")


with st.sidebar:
    st.switch_page("pages/1_🏠_Inicio.py")