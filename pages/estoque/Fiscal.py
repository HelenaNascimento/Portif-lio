import streamlit as st
import pandas as pd
import pyodbc as bd

@st.cache_resource

def show():
   st.write('olá')