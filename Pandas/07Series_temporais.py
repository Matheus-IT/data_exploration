import pandas as pd
import numpy as np

# Criando um range de datas com frequência de mêses
rng = pd.date_range('03/24/2020', periods = 50, freq = 'D')
#Criando a Time Serie(série temporal) com index doo dados que temos no range
ts = pd.Series(np.random.randint(0, 500, len(rng)), index = rng)
print(ts)
