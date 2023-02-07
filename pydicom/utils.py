import numpy as np
from PIL import Image


def show_side_by_side(img1, img2):
    img = Image.fromarray(np.hstack((np.array(img1), np.array(img2))))
    img.show()
    return img
