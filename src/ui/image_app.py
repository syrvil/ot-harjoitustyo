from tkinter import Label, Button, Toplevel, Entry, messagebox, StringVar, Listbox, ACTIVE, SINGLE
from PIL import ImageTk, Image
from config import IMAGE_FILES_PATH
from services.image_manager import image_manager


class ImageApp:
    def __init__(self, master):
        self.master = master
        self.images = []
        self.current_image_index = 0
        self.searched_tag = None
        self.load_images()
        self.create_widgets()

    def load_images(self):
        # Get the images from the image manager Object
        # and add them to the list of images"""

        imgs = image_manager.return_all_images()
        for image in imgs:
            self.images.append(
                (Image.open(IMAGE_FILES_PATH+image.name), image.tags))

    def create_widgets(self):
        self.image_label = Label(self.master)
        self.image_label.grid(row=0, column=1, columnspan=4, padx=10, pady=10)

        self.image_tags = Label(self.master, text="Tags: ")
        self.image_tags.grid(row=1, column=0, columnspan=5, pady=5)

        self.prev_button = Button(
            self.master, text="Previous", command=self.prev_image)
        self.prev_button.grid(row=2, column=1, padx=10, pady=5)

        self.image_order_label = Label(self.master, text="Image 1")
        self.image_order_label.grid(row=2, column=2, padx=10, pady=5)

        self.next_button = Button(
            self.master, text="Next", command=self.next_image)
        self.next_button.grid(row=2, column=3, padx=10, pady=5)

        self.add_tag_button = Button(
            self.master, text="Add Tag", command=self.add_tag)
        self.add_tag_button.grid(row=3, column=1, padx=10, pady=5)

        self.delete_tag_button = Button(
            self.master, text="Delete Tag", command=self.delete_tag)
        self.delete_tag_button.grid(row=3, column=2, padx=10, pady=5)

        self.search_button = Button(
            self.master, text="Search", command=self.search_image)
        self.search_button.grid(row=3, column=3, padx=10, pady=5)

        self.restore_defaults_button = Button(
            self.master, text="Restore Default", command=self.restore_defaults)
        self.restore_defaults_button.grid(row=4, column=0, columnspan=5, pady=5)

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

    def add_tag(self):
        tag_window = Toplevel(self.master)
        tag_window.title("Add Tag")
        tag_label = Label(tag_window, text="Enter tag:")
        tag_label.pack()
        tag_entry = Entry(tag_window)
        tag_entry.pack()
        ok_button = Button(tag_window, text="OK", command=lambda: self.add_tag_to_image(
            tag_entry.get(), tag_window))
        ok_button.pack()

    def add_tag_to_image(self, tag, tag_window):
        if not tag:
            messagebox.showwarning("Invalid tag", "Tag cannot be empty!")
        else:
            image = self.images[self.current_image_index]
            image_tags = image[1]
        if tag not in image_tags:
            image_tags.append(tag)
            self.update_image_tags()
            messagebox.showinfo("Success", f"Tag '{tag}' added to image!")
        else:
            messagebox.showwarning(
                "Tag exists", f"Tag '{tag}' already exists for this image.")
            tag_window.destroy()

    def delete_tag(self):
        image = self.images[self.current_image_index]
        image_tags = image[1]
        if not image_tags:
            messagebox.showwarning("No tags", "This image has no tags.")
        else:
            tag_window = Toplevel(self.master)
            tag_window.title("Delete Tag")
            tag_label = Label(tag_window, text="Select tag to delete:")
            tag_label.pack()
            tag_options = image_tags
            tag_var = StringVar(value=tag_options)
            tag_listbox = Listbox(
                tag_window, listvariable=tag_var, selectmode=SINGLE)
            tag_listbox.pack()
            ok_button = Button(tag_window, text="OK", command=lambda: self.delete_tag_from_image(
                tag_listbox.get(ACTIVE), tag_window))
            ok_button.pack()

    def delete_tag_from_image(self, tag, tag_window):
        image = self.images[self.current_image_index]
        image_tags = image[1]
        if not image_tags:
            messagebox.showwarning("No tags", "This image has no tags.")
        else:
            image_tags.remove(tag)
            self.update_image_tags()
            messagebox.showinfo("Success", f"Tag '{tag}' deleted from image!")
        tag_window.destroy()

    def search_image(self):
        tag_window = Toplevel(self.master)
        tag_window.title("Search Image")
        tag_label = Label(tag_window, text="Enter tag to search:")
        tag_label.pack()
        tag_entry = Entry(tag_window)
        tag_entry.pack()
        ok_button = Button(tag_window, text="OK", command=lambda: self.search_for_tag(
            tag_entry.get(), tag_window))
        ok_button.pack()

    def search_for_tag(self, tag, tag_window):
        if not tag:
            messagebox.showwarning("Invalid tag", "Tag cannot be empty!")
        else:
            image_indices = []
            for i, image in enumerate(self.images):
                if tag in image[1]:
                    image_indices.append(i)
            if not image_indices:
                messagebox.showinfo(
                    "No matches", f"No images found with tag '{tag}'")
            else:
                self.searched_tag = tag
                self.current_image_index = image_indices[0]
                self.update_image()
                self.image_order_label.config(
                    text=f"Image {self.current_image_index+1} of {len(image_indices)}")
        tag_window.destroy()

    def update_image_tags(self):
        image = self.images[self.current_image_index]
        tags = image[1]
        tag_text = "Tags: " + ", ".join(tags)
        self.image_tags.config(text=tag_text)

    def restore_defaults(self):
        pass

    def update_image(self):
        image = self.images[self.current_image_index][0]
        image = image.resize((400, 400), Image.LANCZOS)
        photo = ImageTk.PhotoImage(image)
        self.image_label.config(image=photo)
        self.image_label.image = photo
        self.update_image_tags()
        self.image_order_label.config(
            text=f"Image {self.current_image_index+1} of {len(self.images)}")

# if __name__ == "__main__":
#    root = Tk() # window = Tk()
#    root.title("Image App") # window.title("Image Tagging App")
#    app = ImageApp(root) # ui = ImageApp(window); ui.start()
#    root.mainloop() # window.mainloop()
