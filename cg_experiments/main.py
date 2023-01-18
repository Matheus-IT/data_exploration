import numpy as np
from fractions import Fraction
import functools
import os
import psutil
import multiprocessing as mp
from math import radians
from decimal import Decimal
from rotation_matrices import get_rotation_matrix_x
from scale_matrices import get_uniform_scale_matrix
from translation_matrices import get_translation_matrix

print(get_rotation_matrix_x(90))

print(get_uniform_scale_matrix(10))

print(get_translation_matrix(0, 2, 3))
