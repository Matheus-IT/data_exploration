import pandas as pd
import numpy as np
df = pd.DataFrame(np.random.randn(8, 4), columns = list('abcd'))
print(df)
s = df.iloc[4] #Colocar os valores que estão no indice 4 dentro de s
#Adiciona mais um item no DataFrame df
df = df.append(s, ignore_index = True) #ignore_index=True pra desconsiderar o indice que s já tem
print(df)
