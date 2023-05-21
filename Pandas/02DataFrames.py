from pandas import DataFrame
import numpy as np

'''Dataframes representam uma estrutura tabular semelhante a estrutura de uma planilha do Excel, contendo uma coleção de
colunas em que cada uma pode ser um diferente tipo de valor (número, string, etc...). Os Dataframes possuem index e linhas
e esta estrutura é muito semelhante a um dataframe em R. Os dados de um dataframe são armazenados e um ou mais blocos
bidimensionais, ao invés de listas, dicionários ou alguma outra estrutura de array.'''
frame = DataFrame(
    {
        'Estado': ['Santa Catarina', 'Paraná', 'Goiás', 'Bahia', 'Minas Gerais'],
        'Ano': [2002, 2003, 2004, 2005, 2006],
        'População': [1.5, 1.7, 3.6, 2.4, 2.9],
    },
    index=['um', 'dois', 'tres', 'quatro', 'cinco'],
    columns=['Estado', 'Ano', 'População', 'Débito'],
)
print(frame)


print('Só os estados:')
print(frame['Estado'])
print(f'{frame.index} -> Indices')
print(f'{frame.columns} -> Colunas')
print(f'{frame.values} -> Valores')

print(frame[:2])
frame['Débito'] = np.arange(5.0)
print(frame)
print(frame.describe()) # Mostra um resumo estatístico do DataFrame
print(frame.loc['quatro']) # Localizando esse cara no DataFrame
print(frame.iloc[3]) # Localizando o mesmo cara anterior mas com indexação numerica normal

# CONVERTENDO COLUNA EM INDICE
site_statist = {
    'Dias':[1, 2, 3, 4, 5, 6, 7],
    'Visitantes':[45, 23, 67, 78, 23, 12, 14],
    'Taxas':[11, 22, 33, 44, 55, 66, 77],
}
frame2 = DataFrame(site_statist)
print(frame2)
frame2 = frame2.set_index('Dias') #Transformando a coluna Dias em index
print(frame2)
