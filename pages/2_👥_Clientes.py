import streamlit as st #https://extras.streamlit.app/ / https://cheat-sheet.streamlit.app/
import pyodbc as bd
import pandas as pd
import numpy as np
from streamlit_option_menu import option_menu

st.set_page_config(
    page_title="BI - business intelligence",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded")

st.divider()

st.markdown("""
    <h1 style='text-align: center;'>CLIENTES</h1>
""", unsafe_allow_html=True)

st.divider()


selected = option_menu(None, 
    ["Resumo", "Clientes", "Curva_ABC", "Ficha Finance", "Outros" ], 
    icons=[' ', ' ', ' ', ' ', ' '],
    default_index=0,
    orientation="horizontal")

if selected == "Resumo":
    
    from pages.clientes.Resumo import show as resumo_show
    resumo_show()

if selected == "Clientes":
    from pages.clientes.Cad_Client import show as Cad_Client_show

    Cad_Client_show()
        
if selected == "Curva ABC":
    from pages.clientes.Curva_ABC import show as Curva_ABC_show

    Curva_ABC_show()

if selected == "Ficha Finance":
    from pages.clientes.Ficha_Finan import show as Ficha_Finan_show

    Ficha_Finan_show()
    
if selected == "Outros":
    from pages.clientes.outros import show as outros_show

    outros_show()
    
menu_dict = {
    "Total" : {"fn": "Total"},
    "Cliente" : {"fn": "X Cliente"},
    "Fabricante": {"fn": "X Fabricante"}
}


