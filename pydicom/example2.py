import pydicom
from PIL import Image, ImageFilter
import numpy as np
from utils import show_side_by_side

ds = pydicom.read_file("pydicom/image1.dcm")
img1 = Image.fromarray(np.uint8(ds.pixel_array.astype(float)))
img2 = img1.filter(ImageFilter.BoxBlur(8))
show_side_by_side(img1, img2)
