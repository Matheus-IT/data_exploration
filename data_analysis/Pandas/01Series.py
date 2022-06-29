from pandas import Series
import pandas as pd

'''Series são arrays unidimensionais que contém um array de dados e um array de labels, chamado índice.'''
obj1 = Series([4, 7, -5, 3], index=['a', 'b', 'c', 'd'])
print('\nObj1:')
print(obj1)
print(f'Valores: {obj1.values}')
print(obj1.index)
obj2 = Series([43, 71, -52, 39]) #Posso criar Series sem especificar os índices
print('\nObj2:')
print(obj2)
print(f'Valores: {obj2.values}')
print(obj2.index)
print('obj1[obj1 > 3]:')
print(obj1[obj1 > 3]) #Slice dos objetos que tenham valor maior que 3
print(f'Tenho "b" no obj1? R:{"b" in obj1}') #Verificações simples usando o python

# Criando uma série de dados passando um dicionário como parâmetro
dicio = {'Futebol':5200, 'Tenis': 120, 'Natação':698, 'Volleyball':1550}
# Criando uma série a partir do dicionário
obj3 = Series(dicio)
print('\nObj3:')
print(obj3)
# Criando uma lista
esportes = ['Futebol', 'Tenis', 'Natação', 'Basketball'] #Basketball no lugar de Volleyball
# Criando uma serie e usando uma lista como índice
obj4 = Series(dicio, index=esportes)
print('\nObj4:')
print(obj4) #Basketball vai ficar como valor missing
print('Basketball ficou como NaN porque o item Volleyboll\nda lista não bateu com Basketball do dicionário\n')
print('\npd.isnull(obj4)')
print(pd.isnull(obj4)) #Pergunta pro pandas se tem algum valor nulo (Também pode ser feito assim: print(obj4.isnull()))
print('\nSomando:')
print(obj3 + obj4) #Soma os valores dos indices que tem a mesma relação
obj4.name = 'esportes' #Coloca um nome no obj4
print('\nObj4:')
print(obj4)
