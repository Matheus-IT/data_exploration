import pydicom
from pydicom.data import get_testdata_file
from pydicom.uid import RLELossless


# Compressing using pydicom
path = get_testdata_file("CT_small.dcm")
ds = pydicom.dcmread(path)
ds.compress(RLELossless)
ds.save_as("pydicom/CT_small_rle.dcm")
