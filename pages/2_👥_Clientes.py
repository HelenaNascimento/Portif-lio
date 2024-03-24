import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium

def load_data():
    df = pd.read_csv("pages\dados\cidades.csv") 
    return df

def colorize_client_count(client_count):
    if client_count <= 20:
        return 'red'
    elif client_count <= 40:
        return 'orange'
    elif client_count <= 70:
        return 'blue'
    else:
        return 'green'

def show():
    st.set_page_config(
        page_title="BI - Business Intelligence",
        page_icon="📈",
        layout="wide",
        initial_sidebar_state="expanded"
    )

    st.divider()
    st.markdown("<h1 style='text-align: center;'>BI - Business Intelligence</h1>", unsafe_allow_html=True)
    st.divider()
    
    with st.container(border=True):
            st.markdown("""
                <h2 style='text-align: center;'>Dados Vendas</h2>
            """, unsafe_allow_html=True)

    with st.container(border=True):
        
        col1, col2, col3 = st.columns((1.5, 4.5, 2.0))
    
        with col1:
            st.write('olá')
        with col2:    
            df = load_data()
            
            # Criando o mapa com Folium
            m = folium.Map(location=[df['latitude'].mean(), df['longitude'].mean()], zoom_start=7.45)
            
            # Adicionando marcadores coloridos ao mapa e registrando a quantidade de clientes
            for index, row in df.iterrows():
                icon_color = colorize_client_count(row['cliente'])
                icon = folium.Icon(color=icon_color, icon='star')  # Ícone de estrela
                folium.Marker(
                    location=[row['latitude'], row['longitude']],
                    icon=icon,
                    tooltip=f"Clientes: {row['cliente']}"
                ).add_to(m)
            
            # Exibindo o mapa no Streamlit com legenda
            st_data = st_folium(m, width=500, height=500)
            
            legend = """
            Faixa de cores: | < 20 <span style='color:#FF0000'>■</span> | < 40 <span style='color:#FFA500'>■</span> |< 70 <span style='color:#0000FF'>■</span> |> 70 <span style='color:#008000'>■</span> |
            """
            st.markdown(legend, unsafe_allow_html=True)
            
        with col3:
            
            st.write('olá')
            
if __name__ == "__main__":
    show()
