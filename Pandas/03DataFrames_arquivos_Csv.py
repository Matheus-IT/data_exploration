import pandas as pd
import sys

df = pd.read_csv('salarios.csv')
print(df)

# alternatively
# df = pd.read_table('salarios.csv', sep=',')
# df = pd.read_csv('salarios.csv', names=['a', 'b', 'c', 'd'])

# Salvando em um arquivo csv
df.to_csv(sys.stdout, sep=',')
arquivo = open('destino.csv', 'w+')
arquivo.write(df.to_string())
