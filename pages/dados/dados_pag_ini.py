import pandas as pd

def d_vendas():
    

    Vendas = pd.DataFrame({
    'A': [10.30, 20.5, 30.10, 40.5, 50.15],
    'B': [20.30, 40.10, 60, 80, 100],
    'C': [5.5, 10.30, 15, 20.10, 25],
    'D': [15.5, 30, 45.30, 60.10, 75]})
    return Vendas


def d_estoque():
    

    estoque = pd.DataFrame({
        'X': [100, 10, 50, 5],
        'Y': [20, 40, 60, 80],
        'Z': [5, 10, 15, 20],
        'W': [15, 30, 45, 60]})
    return estoque

def d_financeiro():
    

    finan = pd.DataFrame({
    'X': [10, 20, 30, 40, 50],
    'Y': [20, 40, 60, 80, 100],
    'Z': [5, 10, 15, 20, 25],
    'W': [15, 30, 45, 60, 75]})
    return finan

dados_vendas = d_vendas()
dados_estoque = d_estoque()
dados_financeiro = d_financeiro()