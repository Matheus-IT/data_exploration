import pydicom
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


img_path = "image_processing/images/mammography.dcm"
ds = pydicom.dcmread(img_path)

# Get pixel data and metadata
img = ds.pixel_array

# Convert pixel data to 8-bit integer
img = normalize(img, 0, 255)

x, y, w, h = 300, 200, 600, 400  # simply hardcoded the values
track_window = (x, y, w, h)

roi = img[x:w, y:h]
# Setup the termination criteria, either 10 iteration or move by at least 1 pt
term_crit = (cv.TERM_CRITERIA_EPS | cv.TERM_CRITERIA_COUNT, 10, 1)
roi_hist = cv.calcHist([roi], [0], None, [180], [0, 180])
dst = cv.calcBackProject([roi], [0], roi_hist, [0, 180], 1)

ret, track_window = cv.meanShift(dst, track_window, term_crit)

# Draw it on image
x, y, w, h = track_window
img2 = cv.rectangle(img, (x, y), (x + w, y + h), 255, 2)

# img2 = denormalize(img2, 0, 255)
# img = denormalize(img, 0, 255)

img2 = cv.resize(img2, None, fx=0.1, fy=0.1)
img = cv.resize(img, None, fx=0.1, fy=0.1)

images = cv.hconcat([img, img2])
cv.imshow("images", images)
cv.waitKey(0)
cv.destroyAllWindows()
