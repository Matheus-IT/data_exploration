import sys
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
    QVBoxLayout,
    QSizePolicy,
    QFrame,
)
from PyQt6.QtGui import QPixmap, QImage
from PyQt6.QtCore import Qt


# helpers ---------------------------------------------------------------------
def centroidHistogram(clt):
    # Create a histogram for the clusters based on the pixels in each cluster
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
        cv.rectangle(
            bar,
            (int(x_start), 0),
            (int(end), 100),
            color.astype("uint8").tolist(),
            -1
        )
        x_start = end
    return bar

def addWidgetHCenter(layout, widget):
    layout.addWidget(widget)
    return layout.setAlignment(widget, Qt.AlignmentFlag.AlignHCenter)

def addSpacing(layout, space_amount):
    # Create an empty widget to act as a margin
    margin_widget = QWidget()
    margin_widget.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
    margin_widget.setFixedHeight(space_amount)  # Set the height as the margin size
    layout.addWidget(margin_widget)

def clearLayout(layout):
    if layout is not None:
        while layout.count():
            child = layout.takeAt(0)
            if child.widget() is not None:
                child.widget().deleteLater()
            elif child.layout() is not None:
                clearLayout(child.layout())
# -----------------------------------------------------------------------------


class AppWindow(QWidget):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("PyQt App")
        self.setGeometry(100, 100, 600, 300)

        self.mainLayout = QVBoxLayout()

        # Testing zone --------------------------------------------------------
        colors = [
            (206, 47, 47),
            (157, 131, 131),
            (253, 253, 253),
            (181, 14, 14),
            (195, 191, 191),
        ]
        layout = QVBoxLayout()

        for color in colors:
            rgb_value = f'rgb({", ".join(map(str, color))})'

            background = QFrame()
            background.setStyleSheet(f'background-color: {rgb_value}')

            hLayout = QHBoxLayout(background)

            label = QLabel(rgb_value)
            label.setTextInteractionFlags(Qt.TextInteractionFlag.TextSelectableByMouse)

            hLayout.addWidget(label)
            hLayout.addStretch(1)

            copyButton = QPushButton('COPY')
            copyButton.setStyleSheet("max-width: 250px")
            hLayout.addWidget(copyButton)

            layout.addWidget(background)
        # ---------------------------------------------------------------------
        
        self.mainLayout.addLayout(layout)

        self.uploadButton = self.setupUploadButton()

        self.setLayout(self.mainLayout)
    
    def handle_file_upload_btn(self):
        clearLayout(self.mainLayout)
        self.uploadButton = self.setupUploadButton()

        file_dialog = QFileDialog()
        file_dialog.setNameFilter("Images (*.png *.jpg *.jpeg)")
        file_path, _ = file_dialog.getOpenFileName(self, 'Open Image', './image_processing/images/')
        if not file_path:
            return

        self.chosen_image_file_path = file_path

        pixmap = QPixmap(self.chosen_image_file_path).scaled(250, 250, Qt.AspectRatioMode.KeepAspectRatio)
        lbl = QLabel(parent=self)
        lbl.setPixmap(pixmap)
        addWidgetHCenter(self.mainLayout, lbl)

        if not hasattr(self, 'processButton'):
            self.processButton = QPushButton('PROCESS', parent=self)
            self.processButton.setStyleSheet("max-width: 250px")
            self.processButton.clicked.connect(self.handle_process_chosen_image)
            addWidgetHCenter(self.mainLayout, self.processButton)
    
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

        layout = QVBoxLayout()

        for color in clt.cluster_centers_:
            rgb_value = f'rgb({", ".join(map(str, color.astype("uint8")))})'
            label = QLabel(rgb_value)
            label.setTextInteractionFlags(Qt.TextInteractionFlag.TextSelectableByMouse)
            layout.addWidget(label)
        
        self.mainLayout.addLayout(layout)
        
        h, w, ch = bar.shape
        bytes_per_line = ch * w
        
        image = QImage(bar.data, w, h, bytes_per_line, QImage.Format.Format_RGB888)
        pixmap = QPixmap.fromImage(image).scaled(250, 250, Qt.AspectRatioMode.KeepAspectRatio)
        
        lbl = QLabel(parent=self)
        lbl.setPixmap(pixmap)
        addWidgetHCenter(self.mainLayout, lbl)
    
    def setupUploadButton(self):
        self.uploadButton = QPushButton('UPLOAD', parent=self)
        self.uploadButton.clicked.connect(self.handle_file_upload_btn)
        self.uploadButton.setStyleSheet("max-width: 250px")
        addWidgetHCenter(self.mainLayout, self.uploadButton)


if __name__ == "__main__":
    app = QApplication([])

    window = AppWindow()
    window.show()

    sys.exit(app.exec())
