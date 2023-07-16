import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


data = {
    "Year": [2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023],
    "Documents": [18, 16, 24, 21, 10, 13, 22, 26, 25, 15, 2],
}

df = pd.DataFrame(data)

sns.lineplot(x="Year", y="Documents", data=df, markers=True, markersize=10)

plt.xlabel("Ano")
plt.ylabel("Documentos")
plt.xticks(data["Year"])
plt.show()
