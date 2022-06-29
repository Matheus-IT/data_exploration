import pandas as pd
import numpy as np
#Criando um DataFrame com coluna de datas
data = pd.date_range('20200321', periods=10) #10 dias
df = pd.DataFrame(np.random.randn(10, 4), index = data, columns = list('ABCD')) #Colocando a data como index
print(df)
print(df.mean()) #Cálculo da média das colunas
print(df.mean(1)) #Cálculo da média das linhas
#Usando métodos numpy
df.apply(np.cumsum) #Calcula a soma acumulada
