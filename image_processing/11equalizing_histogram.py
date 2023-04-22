import numpy as np
import matplotlib.pyplot as plt
from PIL import Image


img = Image.open("image_processing/images/cube.jpg").convert("L")
img1 = np.asarray(img)

plt.hist(img1.flatten())
plt.show()

fl = img1.flatten()
hist, bins = np.histogram(img1, 256, [0, 255])

cdf = hist.cumsum()
cdf_m = np.ma.masked_equal(cdf, 0)

num_cdf_m = (cdf_m - cdf_m.min()) * 255
den_cdf_m = cdf_m.max() - cdf_m.min()

cdf_m = num_cdf_m / den_cdf_m

cdf = np.ma.filled(cdf_m, 0).astype("uint8")

img2 = cdf[fl]

img3 = np.reshape(img2, img1.shape)

img4 = np.asarray(img3)

plt.hist(img4.flatten())
plt.show()
