import numpy as np

my_matrix = np.arange(27).reshape(3, 3, 3)

print(my_matrix)
print(my_matrix.sum(axis=0))
print(my_matrix.prod(axis=1))
print(my_matrix.mean(axis=2))
