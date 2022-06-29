from matplotlib import pyplot as plt

idades = [22,65,45,55,21,22,34,42,41,4,99,101,120,122,130,111,115,80,75,54,44,64,13,18,48]
posicoes = [x for x in range(len(idades))]
plt.bar(posicoes, idades)
plt.show()
