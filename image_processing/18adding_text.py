import numpy as np
from utils.elapsed_time import Timer
from PIL import Image
import cv2 as cv


with Timer():
    original = cv.imread("image_processing/images/mammography2.png")
    original = cv.cvtColor(original, cv.COLOR_BGRA2GRAY)
    cv.putText(original, 'Hello', (155, 155), cv.FONT_HERSHEY_SIMPLEX, 3, (250, 220, 250), 4)
    Image.fromarray(original).show()
