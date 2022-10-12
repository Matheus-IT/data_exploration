import numpy as np
import math
from math import pi

u = np.array([-1, 0])
v = np.array([2, 0])

print((np.linalg.norm(u) * np.linalg.norm(v)))

print(
    math.acos(
        np.dot(u, v) / (np.linalg.norm(u) * np.linalg.norm(v)),
    ),
)
