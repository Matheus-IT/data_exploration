import numpy as np
import math
from math import pi

u = np.array([1, 3])
v = np.array([0, 7])

print(np.linalg.norm(u) ** 2)

print(((v * u) * v) / (np.linalg.norm(v) ** 2))
