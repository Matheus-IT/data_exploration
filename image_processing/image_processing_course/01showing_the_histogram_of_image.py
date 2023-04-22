from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

img = Image.open("image_processing/images/cube.jpg").convert("L")
img = np.array(img)
plt.hist(img.flatten())
plt.show()
