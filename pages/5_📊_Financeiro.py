import streamlit as st #https://extras.streamlit.app/ / https://cheat-sheet.streamlit.app/
from streamlit_option_menu import option_menu


st.set_page_config(
    page_title="BI - business intelligence",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded")

st.divider()


st.markdown("""
    <h1 style='text-align: center;'>FINANCEIRO</h1>
""", unsafe_allow_html=True)

st.divider()

selected = option_menu(None, 
    ["Resumo", "Contas a Receber", "Contas a Pagar" ], 
    icons=[' ', ' ', ' ', ' ', ' '],
    default_index=0,
    orientation="horizontal")

if selected == "Resumo":
    
    from pages.financeiro.resumo_fin import show as resumo_fin_show
    
    resumo_fin_show()

if selected == "Contas a Receber":
    from pages.financeiro.cont_receb import show as cont_Receb_show

    cont_Receb_show()
        
if selected == "Contas a Pagar":
    from pages.financeiro.cont_pag import show as cont_Pag_show

    cont_Pag_show()