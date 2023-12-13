import skimage.feature as feature
import numpy as np
import cv2 as cv
from utils.presentation import show_image
import matplotlib.pyplot as plt


class LocalBinaryPatterns:
    def __init__(self, numPoints, radius):
        self.numPoints = numPoints
        self.radius = radius

    def describe(self, image, eps=1e-7):
        lbp = feature.local_binary_pattern(
            image, self.numPoints, self.radius, method="uniform"
        )
        (hist, _) = np.histogram(
            lbp.ravel(),
            bins=np.arange(0, self.numPoints + 3),
            range=(0, self.numPoints + 2),
        )

        # Normalize the histogram
        hist = hist.astype("float")
        hist /= hist.sum() + eps

        return hist, lbp


img = cv.imread("image_processing/images/man.jpg")
img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

desc = LocalBinaryPatterns(24, 8)
hist, lbp = desc.describe(img)

show_image(lbp)
plt.imshow(lbp, cmap="gray")
plt.axis("off")
plt.show()
