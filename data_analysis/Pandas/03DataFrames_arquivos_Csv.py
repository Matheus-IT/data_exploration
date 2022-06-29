import pandas as pd

# Usando read_csv
df = pd.read_csv('salarios.csv') # Importando o arquivo salarios.csv
df = pd.read_table('salarios.csv', sep=',')
print(df)

# Alterando título das colunas com names
df = pd.read_csv('salarios.csv', names=['a', 'b', 'c', 'd'])
print(df)

# Salvando em um arquivo csv
import sys
df.to_csv(sys.stdout, sep=',')
arquivo = open('destino.csv', 'w+')
arquivo.write(df.to_string())
