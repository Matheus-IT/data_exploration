import numpy as np
import pydicom
import matplotlib.pyplot as plt


with pydicom.dcmread("pydicom/image5.dcm") as ds:
    img = ds.pixel_array.astype(np.int16)
    plt.imshow(img, cmap=plt.cm.bone)
    plt.show()
