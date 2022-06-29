from pylab import * #O pylab é a união do matplotlib com o numpy

x = linspace(0, 5, 10)
y = x ** 2
fig = figure()

# Definindo os eixos
axes = fig.add_axes([0.1, 0.1, 0.8, 0.8])
axes.plot(x, y, 'r')
axes.set_xlabel('x')
axes.set_ylabel('y')
axes.set_title('Gráfico de Linha')
show()
