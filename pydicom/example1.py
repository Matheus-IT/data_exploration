import numpy as np
import pydicom
from pydicom.data import get_testdata_file
from PIL import Image


with pydicom.dcmread(get_testdata_file("CT_small.dcm")) as ds:
    image = ds.pixel_array.astype(float)
    rescaled = (np.maximum(image, 0) / image.max()) * 255
    final_image = np.uint8(rescaled)
    Image.fromarray(final_image).show()
