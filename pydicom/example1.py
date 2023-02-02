import numpy as np
import pydicom
from PIL import Image


ds = pydicom.read_file("pydicom/image1.dcm")
image = ds.pixel_array.astype(float)
rescaled = (np.maximum(image, 0) / image.max()) * 255
final_image = np.uint8(rescaled)
Image.fromarray(final_image).show()
