import pydicom
from PIL import Image, ImageFilter
import numpy as np
from utils import show_side_by_side

ds = pydicom.read_file("pydicom/image1.dcm")
img1 = Image.fromarray(np.uint8(ds.pixel_array.astype(float))).convert("L")
img2 = img1.filter(
    ImageFilter.Kernel(
        size=(3, 3),
        kernel=[-1, 0, 1, -2, 0, 2, -1, 0, 1],
        scale=1,
        offset=0,
    )
)
show_side_by_side(img1, img2)
