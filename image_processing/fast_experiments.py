import matplotlib.pyplot as plt
from pydicom.pixel_data_handlers.util import apply_voi_lut
from utils.presentation import (
    show_pixel_info,
    show_voi_lut_module,
    show_file_dataset_info,
    show_pixel_array_info,
)
import cv2 as cv
from utils.image_normalization import normalize, denormalize
from icecream import ic
import numpy as np
from utils.elapsed_time import Timer
from PIL import Image
import pydicom


with Timer():
    MAMMOGRAPHY_DATASET_PATH = "/home/matheuscosta/Documents/mammography-dataset/nbia/CMMD/D1-0001/07-18-2010-NA-NA-79377/1.000000-NA-70244/"
    ds = pydicom.dcmread(MAMMOGRAPHY_DATASET_PATH + "1-1.dcm")
    original = ds.pixel_array
    # Image.fromarray(original).show()
    ic(ds)
