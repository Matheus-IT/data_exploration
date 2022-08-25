from pylab import *

# Gráficos com 2 figuras
x = linspace(0, 5, 10)
y = x ** 2

# Gráficos em Paralelo
fig, axes = subplots(nrows = 1, ncols = 2)

for ax in axes:
    ax.plot(x, y, 'r')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_title('Título')
    
fig.tight_layout()
show()
