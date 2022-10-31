import numpy as np

a = np.array(
    [
        [0, -1, 0, 0],
        [-1, 0, 0, 0],
        [0, 0, -1, -5],
        [0, 0, 0, 1],
    ]
)
b = np.array(
    [
        [0],
        [0],
        [-7],
        [1],
    ]
)

print(np.dot(a, b))
