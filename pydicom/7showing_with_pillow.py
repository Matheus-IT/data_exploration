import numpy as np
import pydicom
from contrib.pydicom_PIL import show_PIL


with pydicom.dcmread("pydicom/image5.dcm") as ds:
    # ------- If I use this method the image colors don't look right ---------
    # img = ds.pixel_array.astype(np.int8)
    # Image.fromarray(img, mode="L").show()
    # ------------------------------------------------------------------------
    show_PIL(ds)
