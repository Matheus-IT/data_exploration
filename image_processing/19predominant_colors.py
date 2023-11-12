import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk


LABEL_IMAGE_SIZE = (200, 200)


class ImageProcessorApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Image Processor")
        self.geometry("500x500")
        self.iconbitmap("image_processing/icons/app_icon.ico") # window icon

        # Load an image
        image = Image.open("image_processing/icons/app_logo.jpg")  # Replace with the actual path to your image
        self.photo = ImageTk.PhotoImage(image.resize(LABEL_IMAGE_SIZE))
        # Create a label to display the image on top of the button
        self.image_label = tk.Label(self, image=self.photo)
        self.image_label.place(relx=0.5, rely=0.5, anchor="center")  # Adjust the position as needed

        # Button to trigger image upload
        upload_button = tk.Button(self, text="Upload Image", command=self.upload_image)
        upload_button.pack(pady=100)

    def upload_image(self):
        # Open a file dialog to select an image file
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])

        if file_path:
            # Open and process the image using PIL
            print(f'Image path {file_path}')
            image = Image.open(file_path)

            # Display the image in the Tkinter window
            photo = ImageTk.PhotoImage(image.resize(LABEL_IMAGE_SIZE))
            self.image_label.config(image=photo)
            self.image_label.image = photo  # to prevent garbage collection

            # Perform your image processing operations here

if __name__ == "__main__":
    app = ImageProcessorApp()
    app.mainloop()
