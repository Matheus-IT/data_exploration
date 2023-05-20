from pandas import Series
import pandas as pd
from icecream import ic

"""Series são arrays que contém um array de dados e um array de labels, chamado índice."""
obj1 = Series([4, 7, -5, 3], index=["a", "b", "c", "d"])
ic(obj1)
print(f"Valores: {obj1.values}")
ic(obj1.index)
obj2 = Series([43, 71, -52, 39])
ic(obj2)
print(f"Valores: {obj2.values}")
ic(obj2.index)
ic(obj1[obj1 > 3])
print(f'Tenho "b" no obj1? R:{"b" in obj1}')


dicio = {"Futebol": 5200, "Tenis": 120, "Natação": 698, "Volleyball": 1550}

obj3 = Series(dicio)
ic(obj3)

esportes = ["Futebol", "Tenis", "Natação", "Basketball"]

obj4 = Series(dicio, index=esportes)
ic(obj4)
print(
    "Basketball ficou como NaN porque o item Volleyboll\nda lista não bateu com Basketball do dicionário\n"
)
ic(pd.isnull(obj4))
print("\nSomando:")
ic(obj3 + obj4)
obj4.name = "esportes"
ic(obj4)
