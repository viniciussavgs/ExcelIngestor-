import pandas as pd
def analisar_colunas(df):
    ''' 
    Analisa as colunas do DataFrame e retorna
    informações sobre nome e tipo de dados.
    '''
    info_colunas = []
    for coluna in df.columns:
        tipo = str(df[coluna].dtype)

        info_colunas.append({
            "nome": coluna,
            "tipo": tipo
        })

    return info_colunas