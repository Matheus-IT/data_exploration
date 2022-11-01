import numpy as np
from icecream import ic

arr = np.array([1, 2, 3, 4, 5])
new_arr = np.array(list(filter(lambda x: x % 2 == 0, arr)))

ic(new_arr)
