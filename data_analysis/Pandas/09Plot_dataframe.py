import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Serie de 500 dias começando em 03/24/2020:
ts = pd.Series(np.random.randn(500), index = pd.date_range('3/24/2020', periods = 500, freq = 'D'))
ts = ts.cumsum() #Aplicando soma acumulada
