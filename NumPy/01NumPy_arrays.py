import numpy as np

# CRIANDO UM ARRAY:
vetor1 = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8])
matrix1 = np.array([[0, 1, 2, 3, 4],
                    [5, 6, 7, 8, 9],
                    [10,11,12,13,14]])
# Cria uma array a partir de um intervalo - np.arange(star, stop-1, step):
vetor2 = np.arange(1, 6, 1)
# Cria um array de zeros com shape(n,m):
zeros = np.zeros(5)
# Cria um array de ums com shape(n, m):
ums = np.ones(5)
# Cria uma matrix diagonal de ordem n:
meye = np.eye(3)
# Cria uma matriz diagonal de ordem n com os valores inseridos:
mdiag = np.diag([1, 2, 3, 4])
# Números espaçados dentro de um intervalo específico:
vlinspace = np.linspace(1, 3, 5)
# Criando matrizes
listas = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrixlistas = np.matrix(listas)

#vetor1[0] = 'Novo elem' # Não posso atribuir elementos de tipos diferentes
print(f'{vetor1} - > vetor1')
print('matrix1:')

for cont in range(matrix1.shape[0]):
    print(matrix1[cont])

print(f'{vetor2} - > vetor2')
print(f'{zeros} -> zeros')
print(f'{ums} -> ums')
print(f'{meye} -> meye')
print(f'{mdiag} -> mdiag')
print(f'{vlinspace} -> vlinspace')
print(f'{matrixlistas} -> matrixlistas')
print(f'{vetor1.dtype} -> vetor1.dtype') # Mostra o tipo dos elementos do array
print(f'{type(vetor1)} -> type(vetor1)')

# ALGUNS ATRIBUTOS ESSENCIAIS
print(f'{matrix1.shape} -> matrix1.shape')
print(f'{matrix1.ndim} -> matrix1.ndim') # Número de dimensões
print(f'{matrix1.size} -> matrix1.size')
