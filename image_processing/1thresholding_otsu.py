"""
Thresholding é uma técnica de segmentação simples e amplamente utilizada que 
separa pixels com base em seus valores de intensidade. Uma técnica de thresholding 
comum para detecção de tumores é o método de Otsu, que calcula um valor de limiar 
ótimo com base no histograma de intensidade da imagem
"""

import cv2
import numpy as np
import pydicom


# Carregar imagem
ds = pydicom.dcmread("image_processing/images/dicom/mammography.dcm")

# Get pixel data and metadata
pixel_data = ds.pixel_array

# Convert pixel data to 8-bit integer
img = cv2.normalize(pixel_data, None, 0, 255, cv2.NORM_MINMAX, cv2.CV_8UC1)

# Resize image, or else it will be displayed too large
img = cv2.resize(img, (0, 0), fx=0.15, fy=0.15)

# Aplicar o método de thresholding de Otsu
ret, thresh = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# Mostrar o resultado
cv2.imshow("Resultado", thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()
