import os
import pandas as pd

data = {'Estado': ['Santa Catarina', 'Paraná', 'Goiás', 'Bahia', 'Minas Gerais'],
        'Ano': [2002, 2003, 2004, 2005, 2006],
        'População': [1.5, 1.7, 3.6, 2.4, 2.9]} #Criamos um dicionário
df = pd.DataFrame(data, index=None) #Pega os dados acima e transforma em um DataFrame
#Verifica se o arquivo existe
try:
    f = open('teste_df.xlsx', 'r')
except:
    print('ERRO: O arquivo não existe')
else:
    df.to_excel('teste_df.xlsx', sheet_name='Sheet1')
df2 = pd.read_excel('teste_df.xlsx', 'Sheet1', index_col=None, na_values=['NA'])
print(df2)
