import pandas as pd 

def ler_excel(caminho_arquivo):
    '''
    lê um arquivo excel e retorna um DataFrame.
    '''
    df = pd.read_excel(caminho_arquivo)
    return df