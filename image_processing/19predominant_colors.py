import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk


class ImageProcessorApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.geometry("500x500")
        self.title("Image Processor")

        # Create a label to display the image
        self.image_label = tk.Label(self)
        self.image_label.pack(padx=10, pady=10)

        # Button to trigger image upload
        upload_button = tk.Button(self, text="Upload Image", command=self.upload_image)
        upload_button.pack(pady=10)

    def upload_image(self):
        # Open a file dialog to select an image file
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])

        if file_path:
            # Open and process the image using PIL
            print(f'Image path {file_path}')
            image = Image.open(file_path)

            # Display the image in the Tkinter window
            photo = ImageTk.PhotoImage(image)
            self.image_label.config(image=photo)
            self.image_label.image = photo  # to prevent garbage collection

            # Perform your image processing operations here

if __name__ == "__main__":
    app = ImageProcessorApp()
    app.mainloop()
