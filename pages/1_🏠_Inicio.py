
import streamlit as st
import pandas as pd
from pages.dados.dados_pag_ini import *

st.set_page_config(
    page_title="BI - business intelligence",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded")


st.divider()

st.markdown("""
    <h1 style='text-align: center;'>BI - business intelligence </h1>
""", unsafe_allow_html=True)

st.divider()

v1 = dados_vendas['A'].sum()
v2 = dados_vendas['B'].sum()
v3 = dados_vendas['C'].sum()
v4 = dados_vendas['D'].sum()
v_t = v1+v2+v3+v4
v_m = (v1+v2+v3+v4)/4

with st.container(border=True):
    st.markdown("""
        <h2 style='text-align: center;'>Dados Vendas</h2>
    """, unsafe_allow_html=True)

with st.container(border=True):
    
    col1, col2, col3 = st.columns((1.5, 4.5, 2.0))
    
    with col1:
        with st.container(border=True):
            st.markdown("""
                <p style='text-align: center;'>Informativo: </p>
            """, unsafe_allow_html=True)
        
        with st.container(border=True):
             st.markdown(f'Dados equivalente as 5 últimas semanadas dos vendedores A: {v1}, B: {v2}, C: {v3}, D: {v4}. Somando um Total de Vendas: {v_t}')
    with col2:
        with st.container():
            tab1, tab2 = st.tabs(["Gráfico de Vendas", "Dados de Vendas"])
            chart_data = pd.DataFrame(dados_vendas, columns=['A', 'B', 'C', 'D'])
            
            with tab1:
                
                st.bar_chart(chart_data)
            
            with tab2:
                
                df = pd.DataFrame(dados_vendas)
                st.table(df)
            
    with col3:
       with st.container(): 
        with st.container(border=True): 
            st.markdown(f'Valor Médio de vendas das últimas 5 semanas e de R${v_m}')
        col4, col5 = st.columns(2)
        
        with col4:
            with st.container(border=True):
                st.metric(label="Vendedor A", value=v1, delta=int(v1-v_m))
            with st.container(border=True):
                st.metric(label="Vendedor C", value=v3, delta=int(v3-v_m))
                
        with col5:
            with st.container(border=True):
                st.metric(label="Vendedor B", value=v2, delta=int(v2-v_m))
            with st.container(border=True):
                st.metric(label="Vendedor D", value=v4, delta=int(v4-v_m))


with st.container(border=True):
    st.markdown("""
        <h2 style='text-align: center;'>Dados Estoque</h2>
    """, unsafe_allow_html=True)

with st.container(border=True):
    
    col1, col2, col3 = st.columns((1.5, 4.5, 2.0))
    
    with col1:
        with st.container(border=True):
            st.markdown("""
                <p style='text-align: center;'>Informativo</p>
            """, unsafe_allow_html=True)
        
        with st.container(border=True):
            st.markdown(f'Dados equivalente as 5 últimas semanadas dos vendedores A: {v1}, B: {v2}, C: {v3}, D: {v4}, Total de Vendas: {v_t}')
    with col2:
        
        with st.container():
            tab1, tab2 = st.tabs(["Gráfico de Vendas", "Dados de Vendas"])
            
            chart_data = pd.DataFrame({
                    'Produto': ['X', 'Y', 'Z', 'W'],
                    'Entrada_Compra': [dados_estoque['X'].iloc[0], dados_estoque['Y'].iloc[0], dados_estoque['Z'].iloc[0], dados_estoque['W'].iloc[0]],
                    'Entrada_Dev': [dados_estoque['X'].iloc[1], dados_estoque['Y'].iloc[1], dados_estoque['Z'].iloc[1], dados_estoque['W'].iloc[1]],
                    'Saida_Venda' : [dados_estoque['X'].iloc[2], dados_estoque['Y'].iloc[2], dados_estoque['Z'].iloc[2], dados_estoque['W'].iloc[2]], 
                    'Saida_Dev': [dados_estoque['X'].iloc[3], dados_estoque['Y'].iloc[3], dados_estoque['Z'].iloc[3], dados_estoque['W'].iloc[3]],
                    
                })
            
            with tab1:
                
                st.table(chart_data)

            with tab2:
                
            
                st.table(chart_data)
                
                
                
                       

    
        
    with col3:
        df = pd.DataFrame(dados_estoque)


        st.table(df)

with st.container(border=True):
    st.markdown("""
        <h2 style='text-align: center;'>Dados Financeiro</h2>
    """, unsafe_allow_html=True)

with st.container(border=True):
    
    col1, col2, col3 = st.columns((1.5, 4.5, 2.0))
    
    with col1:
        with st.container(border=True):
            st.markdown("""
                <p style='text-align: center;'>Informativo</p>
            """, unsafe_allow_html=True)
        
        with st.container(border=True):
            st.markdown(f'Vendedor A: {v1}, Vendedor B: {v2}, Vendedor C: {v3}, Vendedor D: {v4}, Total de Vendas: {v_t}')
    with col2:
        chart_data = pd.DataFrame(dados_financeiro, columns=['A', 'B', 'C', 'D'])
        st.line_chart(chart_data)
    with col3:
        df = pd.DataFrame(dados_financeiro)


        st.table(df)