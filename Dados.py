import streamlit as st
import numpy as np
import pandas as pd
from numpy import random
from numpy.random import default_rng



with st.container(border = True):
    st.title('Media')
    a = random.randint(20, size=(3))
    a2 = a[np.newaxis, :]

    with st.container(border = True):
        st.subheader('Calculando a Médias dos seguintes valores: ')
        st.write(f'Dados: {a2}')
        media = np.average(a2)
        st.write(f'Media: {media}')
        
    code =  ''' 
            st.write('Media')
            a = random.randint(100, size=(6))
            a2 = a[np.newaxis, :]
            
            with st.container(border = True):
            st.subheader('Calculando a Médias dos seguintes valores: ')
            st.write(f'Dados: {a2}')
            media = np.average(a2)
            st.write(f'Media: {media}')'''
            
    with st.expander("Código: "):
        st.code(code, language='python')      
    
    st.write(f'Gráfico de Barras representando os valores: {a2}')      
    chart_data = pd.DataFrame(a2, columns=["a", "b", "c"])
       
    st.bar_chart(chart_data)
                
with st.container(border = True):
    st.title('Mediana')

    with st.container(border = True):
        rng = default_rng()
        numbers = rng.choice(range(1, 20), size=(16,), replace=True)  # Transformando para um array unidimensional

    with st.container(border=True):
            st.subheader('Calculando a Mediana dos seguintes valores:')
            st.write(f'Dados: {numbers}')

            # Calcular a mediana dos números
            mediana =  int(pd.Series(numbers).median())
            
            st.write(f'Mediana: {mediana}')
            
with st.container(border=True):
    st.title('Moda')
    
    with st.container(border = True):
        rng = default_rng()
        numbers = rng.choice(range(1, 20), size=(16,), replace=True)  # Transformando para um array unidimensional

    with st.container(border=True):
            st.subheader('Calculando a Moda dos seguintes valores:')
            st.write(f'Dados: {numbers}')

            # Calcular a mediana dos números
            moda =  pd.Series(numbers).mode().iloc[0]
            
            st.write(f'Moda: {moda}')
            