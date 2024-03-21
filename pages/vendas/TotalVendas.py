import streamlit as st


@st.cache_resource

def show():

   st.write('Olá')
      
if __name__ == "__main__":
    show()