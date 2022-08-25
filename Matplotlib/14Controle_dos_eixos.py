import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 5, 10)

# Controle dos eixos
fig, axes = plt.subplots(1, 3, figsize = (12, 4))

axes[0].plot(x, x**2, x, x**3)
axes[0].set_title("Eixos com range padrão")

axes[1].plot(x, x**2, x, x**3)
axes[1].axis('tight')
axes[1].set_title("Eixos menores")

axes[2].plot(x, x**2, x, x**3)
axes[2].set_ylim([0, 60])
axes[2].set_xlim([2, 5])
axes[2].set_title("Eixos customizados")
plt.show()
