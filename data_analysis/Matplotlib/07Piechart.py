from matplotlib import pyplot as plt

fatias = [7, 2, 2, 13]
atividades = ['dormir','comer','trabalhar','passear']
colunas = ['c','m','r','k']
plt.pie(fatias, labels = atividades, colors = colunas, startangle = 90, shadow = True, explode = (0,0.1,0,0))
plt.show()
