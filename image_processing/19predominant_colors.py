import sys
from time import sleep
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
    QApplication,
)
from functools import partial
from PyQt6.QtGui import QPixmap, QImage
from PyQt6.QtCore import Qt, QMimeData


# helpers ---------------------------------------------------------------------
def plotColors(hist, centroids):
    # Create our blank barchart
    bar = np.zeros((100, 500, 3), dtype="uint8")

    x_start = 0
    # iterate over the percentage and dominant color of each cluster
    for percent, color in zip(hist, centroids):
        # plot the relative percentage of each cluster
        end = x_start + (percent * 500)
        cv.rectangle(
            bar, (int(x_start), 0), (int(end), 100), color.astype("uint8").tolist(), -1
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
    while layout.count():
        child = layout.takeAt(0)
        if child.widget():
            child.widget().deleteLater()


# -----------------------------------------------------------------------------


class AppWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Image Processor")
        self.setGeometry(100, 100, 600, 300)

        self.container = QHBoxLayout()
        self.mainLayout = QVBoxLayout()
        mainLayoutContainer = QWidget()
        mainLayoutContainer.setFixedWidth(250)

        self.actionButtonsLayout = QHBoxLayout()
        self.imageLayout = QHBoxLayout()

        pixmap = QPixmap("image_processing/icons/app_logo.jpg").scaled(
            230, 230, Qt.AspectRatioMode.KeepAspectRatio
        )
        self.mainImageLbl = QLabel(parent=self)
        self.mainImageLbl.setPixmap(pixmap)
        addWidgetHCenter(self.imageLayout, self.mainImageLbl)

        self.mainLayout.addLayout(self.imageLayout)
        self.mainLayout.addLayout(self.actionButtonsLayout)

        mainLayoutContainer.setLayout(self.mainLayout)
        self.container.addWidget(mainLayoutContainer)

        self.uploadButton = self.setupUploadButton()

        # initializing side layout to be used latter
        self.sideLayout = QVBoxLayout()
        self.container.addLayout(self.sideLayout)

        self.setLayout(self.container)

    def handle_file_upload_btn(self):
        file_dialog = QFileDialog()
        file_dialog.setNameFilter("Images (*.png *.jpg *.jpeg)")
        file_path, _ = file_dialog.getOpenFileName(
            self, "Open Image", "./image_processing/images/"
        )
        if not file_path:
            return

        self.chosen_image_file_path = file_path

        pixmap = QPixmap(self.chosen_image_file_path).scaled(
            230, 230, Qt.AspectRatioMode.KeepAspectRatio
        )
        self.mainImageLbl.setPixmap(pixmap)

        if not hasattr(self, "processButton"):
            self.processButton = QPushButton("PROCESS", parent=self)
            self.processButton.setStyleSheet("max-width: 250px")
            self.processButton.clicked.connect(self.handle_process_chosen_image)
            addWidgetHCenter(self.actionButtonsLayout, self.processButton)

    def handle_process_chosen_image(self):
        from sklearn.cluster import KMeans

        self.image_to_process = cv.imread(self.chosen_image_file_path)

        # We reshape our image into a list of RGB pixels
        self.image_to_process = cv.cvtColor(self.image_to_process, cv.COLOR_BGR2RGB)
        self.image_to_process = self.image_to_process.reshape(
            (self.image_to_process.shape[0] * self.image_to_process.shape[1], 3)
        )

        number_of_clusters = 5
        clt = KMeans(number_of_clusters)
        clt.fit(self.image_to_process)

        clearLayout(self.sideLayout)

        for color in clt.cluster_centers_:
            rgbValue = (
                f'rgb({", ".join(map(lambda channel: str(round(channel)), color))})'
            )

            background = QFrame()
            background.setStyleSheet(f"background-color: {rgbValue}")

            hLayout = QHBoxLayout(background)

            label = QLabel(rgbValue)
            label.setTextInteractionFlags(Qt.TextInteractionFlag.TextSelectableByMouse)

            hLayout.addWidget(label)
            hLayout.addStretch(1)

            copyButton = QPushButton("COPY")
            copyButton.setStyleSheet("width: 50px")
            copyButton.clicked.connect(partial(self.copyText, rgbValue))
            hLayout.addWidget(copyButton)

            self.sideLayout.addWidget(background)

    def setupUploadButton(self):
        self.uploadButton = QPushButton("UPLOAD", parent=self)
        self.uploadButton.clicked.connect(self.handle_file_upload_btn)
        self.uploadButton.setStyleSheet("max-width: 250px")
        addWidgetHCenter(self.actionButtonsLayout, self.uploadButton)

    def copyText(self, rgb_value):
        # Create a QMimeData object to hold the text
        mime_data = QMimeData()
        mime_data.setText(rgb_value)
        # Access the clipboard and set its data to the QMimeData object
        clipboard = QApplication.clipboard()
        clipboard.setMimeData(mime_data)


if __name__ == "__main__":
    app = QApplication([])

    window = AppWindow()
    window.show()

    sys.exit(app.exec())
