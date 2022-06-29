import matplotlib as mpl
import matplotlib.pyplot as plt

x = [1, 3, 5]
y = [2, 5, 7]
plt.plot(x, y, label='Primeira linha')
plt.legend()
plt.xlabel('Variável 1')
plt.ylabel('Variável 2')
plt.title('Teste Plot')
plt.show() #plot(x, y)
