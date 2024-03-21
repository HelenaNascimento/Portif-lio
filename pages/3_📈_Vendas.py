import streamlit as st
from streamlit_option_menu import option_menu

st.set_page_config(
    page_title="BI - business intelligence",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded")

st.divider()

st.markdown("""
    <h1 style='text-align: center;'>VENDAS</h1>
""", unsafe_allow_html=True)

st.divider()

selected = option_menu(None, 
    ["Resumo", "X Cliente", "X Fabricante", "X_Produto", "X Vendedor" ], 
    icons=[' ', ' ', ' ', ' ', ' '],
    default_index=0,
    orientation="horizontal")

if selected == "Resumo":
    
    from pages.vendas.TotalVendas import show as total_vendas_show
    total_vendas_show()

if selected == "X Cliente":
    from pages.vendas.VendasCliente import show as vendas_cliente_show

    vendas_cliente_show()
        
if selected == "X Fabricante":
    from pages.vendas.VendasFabri import show as vendas_fabri_show

    vendas_fabri_show()

if selected == "X Produto":
    from pages.vendas.VendasProduto import show as vendas_Produ_show

    vendas_Produ_show()
    
if selected == "X Vendedor":
    from pages.vendas.VendasVendedor import show as vendas_Vended_show

    vendas_Vended_show()
    
menu_dict = {
    "Total" : {"fn": "Total"},
    "Cliente" : {"fn": "X Cliente"},
    "Fabricante": {"fn": "X Fabricante"}
}


