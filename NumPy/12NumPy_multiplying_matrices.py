import numpy as np
import math
from math import pi, cos, sin, radians


t = np.array(
    [
        [1, 0, -40],
        [0, 1, 30],
        [0, 0, 1],
    ]
)

r = np.array(
    [
        [cos(radians(-90)), -sin(radians(-90)), 0],
        [sin(radians(-90)), cos(radians(-90)), 0],
        [0, 0, 1],
    ]
)

s = np.array(
    [
        [0.5, 0, 0],
        [0, -2, 0],
        [0, 0, 1],
    ]
)

m2 = np.array(
    [
        [0, 1, 0],
        [-1, 0, 0],
        [0, 0, 1],
    ]
)

# m3 = m2.dot(s)
m3 = s.dot(m2)
print(cos(radians(30)))
