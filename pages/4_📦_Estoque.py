import streamlit as st
from streamlit_option_menu import option_menu

st.set_page_config(
    page_title="BI - business intelligence",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded")

st.divider()


st.markdown("""
    <h1 style='text-align: center;'>ESTOQUE</h1>
""", unsafe_allow_html=True)

st.divider()

selected = option_menu(None, 
    ["Resumo", "Produto", "Fabricante", "Fiscal"], 
    icons=[' ', ' ', ' ', ' ', ' '],
    default_index=0,
    orientation="horizontal")

if selected == "Resumo":
    
    from pages.estoque.Resumo import show as resumo_show
    resumo_show()

if selected == "Produto":
    from pages.estoque.Produtos import show as produtos_show

    produtos_show()
        
if selected == "Fabricante":
    from pages.estoque.Fabricante import show as fabricante_show

    fabricante_show()

if selected == "Fiscal":
    from pages.estoque.Fiscal import show as fiscal_show

    fiscal_show()
    
menu_dict = {
    "Total" : {"fn": "Resumo"},
    "Cliente" : {"fn": "Produto"},
    "Fabricante": {"fn": "Fabricante"},
    "Fiscal": {"fn": "Fiscal"}
}


