import numpy as np
import math
from math import pi


a = np.array([0, 1, 5])
b = np.array([0, 1, 0])

w = a / np.linalg.norm(a)

u = np.cross(b, w) / np.linalg.norm(np.cross(b, w))

print('=' * 40)
print(w)
print('=' * 40)
