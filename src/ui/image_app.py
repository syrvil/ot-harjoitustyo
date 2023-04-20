from tkinter import Label, Button, Toplevel, Entry, messagebox, StringVar, Listbox, ACTIVE, SINGLE, filedialog
#from tkinter import *
from PIL import ImageTk, Image
from services.image_manager import image_manager



class ImageApp:
    def __init__(self, master):
        self.master = master
        self.images = None
        self.current_image_index = 0
        self.current_view = None
        self.all_images = None
        self.searched_images = None
        self.loaded_images = None
        self.searched_tag = None
        self.load_images()
        self.create_widgets()

    def load_images(self):
        image_manager.load_images_from_file()
        # A list of Image objects
        self.all_images = image_manager.get_all_images()
        self.current_view = "All Images"

    def create_widgets(self):
        # Upper menu
        self.add_new_button = Button(
            self.master, text="Add New", command=self.add_images)
        self.add_new_button.grid(row=0, column=1, padx=5, pady=5)

        self.search_button = Button(
            self.master, text="Search", command=self.search_image)
        self.search_button.grid(row=0, column=2, padx=10, pady=5)
        
        self.show_all_button = Button(
            self.master, text="Show All", command=self.show_all)
        self.show_all_button.grid(row=0, column=3, padx=5, pady=5)
        
        # View
        self.image_view = Label(self.master, text="All Images")
        self.image_view.grid(row=1, column=0, columnspan=5, pady=5)

        # Image
        self.image_label = Label(self.master)
        self.image_label.grid(row=2, column=1, columnspan=4, padx=10, pady=10)

        # Lower menu    
        self.image_tags = Label(self.master, text="Tags: ")
        self.image_tags.grid(row=3, column=0, columnspan=5, pady=5)

        self.prev_button = Button(
            self.master, text="Previous", command=self.prev_image)
        self.prev_button.grid(row=4, column=1, padx=10, pady=5)

        self.image_order_label = Label(self.master, text="Image 1")
        self.image_order_label.grid(row=4, column=2, padx=10, pady=5)

        self.next_button = Button(
            self.master, text="Next", command=self.next_image)
        self.next_button.grid(row=4, column=3, padx=10, pady=5)

        self.add_tag_button = Button(
            self.master, text="Add Tag", command=self.add_tag)
        self.add_tag_button.grid(row=5, column=1, padx=10, pady=5)

        self.delete_tag_button = Button(
            self.master, text="Delete Tag", command=self.delete_tag)
        self.delete_tag_button.grid(row=5, column=2, padx=10, pady=5)

        self.save_button = Button(
            self.master, text="Save", command=self.save_image)
        self.save_button.grid(row=5, column=3, padx=5, pady=5)


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
            if image_manager.add_tag(image, tag):
                messagebox.showinfo("Success", f"Tag '{tag}' added to image!")
                self.update_image_tags()
            else:
                messagebox.showwarning(
                    "Tag exists", f"Tag '{tag}' already exists for this image.")
                tag_window.destroy()

    def delete_tag(self):
        image = self.images[self.current_image_index]
        image_tags = image.tags
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
                tag_listbox.get(ACTIVE), tag_window, image))
            ok_button.pack()

    def delete_tag_from_image(self, tag, tag_window, image):
        if image_manager.delete_tag(image, tag):
            self.update_image_tags()
            messagebox.showinfo("Success", f"Tag '{tag}' deleted from image!")
        else:
            # this is unneccesaary because tag are selected from a list
            messagebox.showwarning("No tags", "This image has no tags.")
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
            search_results = image_manager.search_for_tag(tag)
            if not search_results:
                messagebox.showinfo(
                    "No matches", f"No images found with tag '{tag}'")
            else:
                self.images.clear()
                self.searched_images = search_results
                self.current_image_index = 0
                self.current_view = "Search Results"
                self.update_image()
        tag_window.destroy()

    def update_image_tags(self):
        image = self.images[self.current_image_index]
        tags = image.tags
        tag_text = "Tags: " + ", ".join(tags)
        self.image_tags.config(text=tag_text)

    def show_all(self):
        self.current_view = "all"
        self.images.clear()
        self.current_image_index = 0
        self.load_images()
        self.update_image()

    def add_images(self):
        files = filedialog.askopenfilenames(initialdir="./src/entities/images/samples", 
                                          title="Select file(s)", 
                                          filetypes=(("jpg files", "*.jpg"), ("all files", "*.*")))
        if files:
            self.images.clear()
            self.loaded_images = image_manager.load_images(files) 
            messagebox.showinfo("Image Loaded", f"Image '{files}' loaded!")
            self.current_view = "Load Images"
            self.current_image_index = 0
            self.update_image()

    def save_image(self):
        if self.current_view == "Load Images":
            self.all_images.extend(self.loaded_images) # logc to ImageManager?
            messagebox.showinfo("New Images Added!", "New images added to database!")
            # add all images to database
        elif self.current_view == "Search Results":
            messagebox.showinfo("Changes saved!", "Changes saved to database!")
            # update database with new tags
        elif self.current_view == "All Images":
            messagebox.showinfo("Changes saved!", "Changes saved to database!")
            # update database with new tags

    def update_image(self):
        if self.current_view == "All Images":
            self.images = self.all_images
        elif self.current_view == "Search Results":
            self.images = self.searched_images
        elif self.current_view == "Load Images":
            self.images = self.loaded_images

        self.image_view.config(text=self.current_view.title())

        image = self.images[self.current_image_index].picture
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
