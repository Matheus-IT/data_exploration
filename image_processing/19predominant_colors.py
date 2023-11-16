import sys
from PIL import Image
import cv2 as cv
import numpy as np
from PyQt6.QtWidgets import QApplication, QLabel, QWidget


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


# class ImageProcessorApp(tk.Tk):
#     def __init__(self):
#         super().__init__()

#         self.title("Image Processor")
#         self.geometry("500x500")
#         self.iconbitmap("image_processing/icons/app_icon.ico") # window icon

#         # Button to trigger image upload
#         upload_button = tk.Button(self, text="Upload Image", command=self.upload_image)
#         upload_button.place(relx=0.5, y=50, anchor='center')

#         # Center image - starts with the app logo
#         image = Image.open("image_processing/icons/app_logo.jpg")
#         self.photo = ImageTk.PhotoImage(image.resize(LABEL_IMAGE_SIZE))
#         # Create a label to display the image on top of the button
#         self.image_label = tk.Label(self, image=self.photo)
#         self.image_label.place(relx=0.5, y=upload_button.winfo_y()+200, anchor='center')

#         process_button = tk.Button(self, text='Process colors', command=self.process_image_colors)
#         process_button.place(relx=0.5, y=self.image_label.winfo_y()+350, anchor='center')

#     def upload_image(self):
#         # Open a file dialog to select an image file
#         file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])

#         if file_path:
#             self.image_to_process = file_path

#             # Display the image in the Tkinter window
#             photo = ImageTk.PhotoImage(Image.open(file_path).resize(LABEL_IMAGE_SIZE))
#             self.image_label.config(image=photo)
#             self.image_label.image = photo  # to prevent garbage collection

#     def process_image_colors(self):
#         from sklearn.cluster import KMeans

#         self.image_to_process = cv.imread(self.image_to_process)
#         # We reshape our image into a list of RGB pixels
#         self.image_to_process = cv.cvtColor(self.image_to_process, cv.COLOR_BGR2RGB)
#         self.image_to_process = self.image_to_process.reshape((self.image_to_process.shape[0] * self.image_to_process.shape[1], 3))

#         number_of_clusters = 5
#         clt = KMeans(number_of_clusters)
#         clt.fit(self.image_to_process)

#         hist = centroidHistogram(clt)
#         bar = plotColors(hist, clt.cluster_centers_)
#         bar = Image.open("image_processing/icons/app_logo.jpg")
#         photo = ImageTk.PhotoImage(bar.resize(LABEL_IMAGE_SIZE))
#         # Create a label to display the image on top of the button
#         self.result_image = tk.Label(self, image=photo)
#         self.result_image.pack()


if __name__ == "__main__":
    app = QApplication([])

    window = QWidget()
    window.setWindowTitle("PyQt App")
    window.setGeometry(100, 100, 600, 500)
    helloMsg = QLabel("<h1>Hello, World!</h1>", parent=window)
    helloMsg.move(60, 15)
    
    window.show()

    # 5. Run your application's event loop
    sys.exit(app.exec())
