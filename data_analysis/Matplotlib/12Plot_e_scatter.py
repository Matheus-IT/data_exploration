import matplotlib.pyplot as plt
import numpy as np

#Plot e scatter
fig = plt.figure()
ax1 = fig.add_subplot(1, 2, 1)
ax1.plot(np.random.randn(50), color='red')
ax2 = fig.add_subplot(1, 2, 2)
ax2.scatter(np.arange(50), np.random.randn(50))
plt.show()
