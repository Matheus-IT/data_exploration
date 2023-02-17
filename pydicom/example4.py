from PIL import Image
import pydicom
from pydicom.data import get_testdata_file
from utils import show_side_by_side
import numpy as np


def grayscale(colored_img):
    w, h = colored_img.size
    img = Image.new("RGB", (w, h))

    for i in range(w):
        for j in range(h):
            pixel = colored_img.getpixel((i, j))
            luminance = (pixel[0] + pixel[1] + pixel[2]) // 3
            img.putpixel((i, j), (luminance, luminance, luminance))
    return img


ds = pydicom.read_file("pydicom/image1.dcm")
img1 = Image.fromarray(ds.pixel_array.astype("uint8"))
show_side_by_side(img1, grayscale(img1))
