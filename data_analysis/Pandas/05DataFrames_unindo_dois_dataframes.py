import pandas as pd
left = pd.DataFrame({'chave':['chave1', 'chave2'], 'coluna1':[1, 2]})
right = pd.DataFrame({'chave':['chave1', 'chave2'], 'coluna2':[4, 5]})
print(left)
print(right)
print(pd.merge(left, right, on='chave'))
