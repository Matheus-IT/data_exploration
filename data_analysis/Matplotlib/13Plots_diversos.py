import matplotlib.pyplot as plt
import numpy as np

_, ax = plt.subplots(2,3)

ax[0,1].plot(np.random.randn(50), color = 'green', linestyle = '-')
ax[1,0].hist(np.random.randn(50))
ax[1,2].scatter(np.arange(50), np.random.randn(50), color = 'red')
plt.show()
