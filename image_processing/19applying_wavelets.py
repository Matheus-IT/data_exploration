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
import pywt


with Timer():
    MAMMOGRAPHY_DATASET_PATH = "/home/matheuscosta/Documents/mammography-dataset/nbia/CMMD/D1-0001/07-18-2010-NA-NA-79377/1.000000-NA-70244/"
    ds = pydicom.dcmread(MAMMOGRAPHY_DATASET_PATH + "1-1.dcm")
    original = ds.pixel_array

    # original = cv.imread("image_processing/images/mammography.png", cv.IMREAD_GRAYSCALE)

    # Aplicar a transformada wavelet (por exemplo, usando a wavelet de Haar)
    coeffs = pywt.dwt2(original, "haar")

    # Obter os coeficientes de detalhe da transformada
    LL, (LH, HL, HH) = coeffs

    # Calcular o valor absoluto dos coeficientes de detalhe
    LH_abs = np.abs(LH)
    HL_abs = np.abs(HL)
    HH_abs = np.abs(HH)

    # Aplicar a limiarização adaptativa para remover ruídos
    threshold = 20
    LH_thresholded = cv.adaptiveThreshold(
        np.uint8(LH_abs), 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 3, threshold
    )
    HL_thresholded = cv.adaptiveThreshold(
        np.uint8(HL_abs), 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 3, threshold
    )
    HH_thresholded = cv.adaptiveThreshold(
        np.uint8(HH_abs), 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 3, threshold
    )

    # Combinar os coeficientes thresholded para obter uma imagem de detecção de nódulos
    nodule_detection = LH_thresholded | HL_thresholded | HH_thresholded

    plt.figure(figsize=(10, 10)), plt.subplot(121), plt.imshow(
        original, cmap="gray"
    ), plt.title("Imagem original"), plt.subplot(122), plt.imshow(
        nodule_detection, cmap="gray"
    ), plt.title(
        "Imagem segmentada"
    ), plt.show()
