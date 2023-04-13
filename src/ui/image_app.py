from tkinter import Label, Button
from PIL import ImageTk, Image
from repositories.file_repository import FileRepository
from config import IMAGE_FILES_PATH


class ImageApp:
    def __init__(self, master):
        self.master = master
        self.images = []
        self.current_image_index = 0
        self.load_images()
        self.create_widgets()
        #print("IMAGE FILE:", IMAGE_FILENAME)
        #print("IMAGE FILE PATH:", IMAGE_FILE_PATH)
        #rint(FileRepository.__dict__)

    def load_images(self):
        #self.images.append(Image.open("src/entities/images/im65.jpg"))
        #self.images.append(Image.open("src/entities/images/im94.jpg"))
        #self.images.append(Image.open("src/entities/images/im112.jpg"))
        imgs = FileRepository()
        for image in imgs.read_images():
            self.images.append((Image.open(IMAGE_FILES_PATH+image.name), image.tags))

    def create_widgets(self):
        self.image_label = Label(self.master)
        self.image_label.grid(row=0, column=1, columnspan=3, padx=10, pady=10)

        self.prev_button = Button(self.master, text="Previous", command=self.prev_image)
        self.prev_button.grid(row=1, column=1, padx=10, pady=5)

        self.image_order_label = Label(self.master, text="Image 1")
        self.image_order_label.grid(row=1, column=2, padx=10, pady=5)

        self.next_button = Button(self.master, text="Next", command=self.next_image)
        self.next_button.grid(row=1, column=3, padx=10, pady=5)

        self.image_tags = Label(self.master, text="Tags: ")
        self.image_tags.grid(row=2, column=0, columnspan=4 , pady=5)

        self.update_image()

    def prev_image(self):
        if self.current_image_index == 0:
            self.current_image_index = len(self.images) - 1
        else:
            self.current_image_index -= 1
        self.update_image()

    def next_image(self):
        if self.current_image_index == len(self.images) - 1:
            self.current_image_index = 0
        else:
            self.current_image_index += 1
        self.update_image()

    def update_image(self):
        image = self.images[self.current_image_index][0]
        image = image.resize((400, 400), Image.LANCZOS)
        photo = ImageTk.PhotoImage(image)
        self.image_label.config(image=photo)
        self.image_label.image = photo
        self.image_order_label.config(text=f"Image {self.current_image_index + 1}")
        self.image_tags.config(text=f"Tags: {self.images[self.current_image_index][1]}")

#if __name__ == "__main__":
#    root = Tk() # window = Tk()
#    root.title("Image App") # window.title("Image Tagging App")
#    app = ImageApp(root) # ui = ImageApp(window); ui.start() 
#    root.mainloop() # window.mainloop()
