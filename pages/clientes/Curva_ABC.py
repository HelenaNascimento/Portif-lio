import streamlit as st

@st.cache_resource

def show():
    st.writer('olá')