import numpy as np

#SLICING DE ARRAYS
a = np.diag([1, 2, 3])
print(a[1, 1]) #2
print(a[2]) #[0 0 3]
b = np.arange(10)
print(b[2:7:2]) #start : stop : step
#VERIFICAR IGUALDADE
a = np.array([1, 2, 3, 4])
b = np.array([2, 2, 1, 3])
print(a==b) #[False True False False]
print(np.array_equal(a, b)) #False
#VALOR MÍNIMO E MÁXIMO
print(a.min()) #1
print(a.max()) #4
#SOMANDO UM ELEMENTO A CADA ITEM NO ARRAY
print(np.array([1, 2, 3]) + 1.5) #[2.5, 3.5, 4.5]
#USANDO O MÉTODO AROUND
a = np.array([1.2, 1.5, 1.6, 2.5, 3.5, 4.5])
b = np.around(a) #Arredonda os valoes
print(b) #[1. 2. 2. 2. 4. 4.]
#COPIANDO UM ARRAY
b = np.array([1, 2, 3, 4])
c = b.flatten()
print(c) #[1 2 3 4]
c = np.copy(b)
print(c) #[1 2 3 4]
#REPETINDO OS ELEMENTOS DE UM ARRAY
v = np.array([1, 2, 3, 4, 5])
print(np.repeat(v, 3)) #[1 1 1 2 2 2 3 3 3 4 4 4 5 5 5]
v = np.array([1, 2, 3, 4, 5])
print(np.tile(v, 3)) #[1 2 3 4 5 1 2 3 4 5 1 2 3 4 5]
#CONCATENANDO ARRAYS
v = np.array([1, 2, 3])
w = np.array([4, 5])
print(np.concatenate((v, w)))
#ADICIONANDO DIMENSÕES AO ARRAY
v = np.array([1, 2, 3])
print(v[:, np.newaxis], v[:,np.newaxis].shape, v[np.newaxis,:].shape)
