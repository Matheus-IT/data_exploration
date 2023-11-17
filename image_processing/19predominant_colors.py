import sys
import typing
from PIL import Image
from PyQt6 import QtCore
import cv2 as cv
import numpy as np
from PyQt6.QtWidgets import (
    QApplication,
    QLabel,
    QWidget,
    QPushButton,
    QFileDialog,
    QHBoxLayout,
)
from PyQt6.QtGui import QPixmap, QImage
from PyQt6.QtCore import Qt


# helpers ---------------------------------------------------------------------
def centroidHistogram(clt):
    # Create a histrogram for the clusters based on the pixels in each cluster
    # Get the labels for each cluster
    numLabels = np.arange(0, len(np.unique(clt.labels_)) + 1)

    # Create our histogram 
    (hist, _) = np.histogram(clt.labels_, bins = numLabels)

    # normalize the histogram, so that it sums to one
    hist = hist.astype("float")
    hist /= hist.sum()

    return hist

def plotColors(hist, centroids):
    # Create our blank barchart
    bar = np.zeros((100, 500, 3), dtype = "uint8")

    x_start = 0
    # iterate over the percentage and dominant color of each cluster
    for (percent, color) in zip(hist, centroids):
      # plot the relative percentage of each cluster
      end = x_start + (percent * 500)
      cv.rectangle(bar, (int(x_start), 0), (int(end), 100),
        color.astype("uint8").tolist(), -1)
      x_start = end
    return bar
# -----------------------------------------------------------------------------


class AppWindow(QWidget):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("PyQt App")
        self.setGeometry(100, 100, 600, 500)

        helloMsg = QLabel("<h1>Hello, World!</h1>", parent=self)
        helloMsg.move(60, 15)

        uploadButton = QPushButton('UPLOAD', parent=self)
        uploadButton.clicked.connect(self.handle_file_upload_btn)
        
        self.hBoxLayout = QHBoxLayout()
        self.hBoxLayout.addWidget(uploadButton)
        self.setLayout(self.hBoxLayout)
    
    def handle_file_upload_btn(self):
        file_dialog = QFileDialog()
        file_dialog.setNameFilter("Images (*.png *.jpg *.jpeg)")
        file_path, _ = file_dialog.getOpenFileName(self, 'Open Image', '.')
        self.chosen_image_file_path = file_path

        pixmap = QPixmap(self.chosen_image_file_path).scaled(250, 250, Qt.AspectRatioMode.KeepAspectRatio)
        lbl = QLabel(parent=self)
        lbl.setPixmap(pixmap)
        self.hBoxLayout.addWidget(lbl)

        process_button = QPushButton('PROCESS', parent=self)
        process_button.clicked.connect(self.handle_process_chosen_image)
        self.hBoxLayout.addWidget(process_button)
    
    def handle_process_chosen_image(self):
        from sklearn.cluster import KMeans

        self.image_to_process = cv.imread(self.chosen_image_file_path)

        # We reshape our image into a list of RGB pixels
        self.image_to_process = cv.cvtColor(self.image_to_process, cv.COLOR_BGR2RGB)
        self.image_to_process = self.image_to_process.reshape((self.image_to_process.shape[0] * self.image_to_process.shape[1], 3))

        number_of_clusters = 5
        clt = KMeans(number_of_clusters)
        clt.fit(self.image_to_process)

        hist = centroidHistogram(clt)
        bar = plotColors(hist, clt.cluster_centers_)
        
        h, w, ch = bar.shape
        bytes_per_line = ch * w
        image = QImage(bar.data, w, h, bytes_per_line, QImage.Format.Format_RGB888)
        pixmap = QPixmap.fromImage(image).scaled(250, 250, Qt.AspectRatioMode.KeepAspectRatio)
        lbl = QLabel(parent=self)
        lbl.setPixmap(pixmap)
        self.hBoxLayout.addWidget(lbl)


if __name__ == "__main__":
    app = QApplication([])

    window = AppWindow()
    window.show()

    sys.exit(app.exec())
