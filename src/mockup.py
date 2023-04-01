import json
import sys

class Id:
    id = 0
    @classmethod
    def next_id(cls):
        cls.id += 1 # or Id.id += 1
        return cls.id # return Id.id

class Image:
    def __init__(self, name, tags):
        self.name = name
        self.tags = tags
        Id.next_id()
        self.id = Id.id

    def __str__(self):
        return f"[{self.id}] name: {self.name} tags: {self.tags}"

class Tags:
    pass

class FileHandler:
    def __init__(self, filename):
        self.filename = filename

    def read(self):
        try:
            with open(self.filename, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            print(f"File {self.filename} not found")

class ImageManager:
    def __init__(self):
        # list to store image objects
        self.image_list = []

    def add_image_to_image_list(self, image: dict):
        # add imgage to image list as an Image object
        self.image_list.append(Image(image["name"], image["tags"]))

    def return_image(self, id):
        # return image object
        for image in self.image_list:
            if image.id == id:
                return image
        return None

    def return_images(self):
        return self.image_list

class ImageManagerApp:
    def __init__(self):
        # create an image manager object
        self.image_manager = ImageManager()
        self.file_handlerer = None

    def load_images(self):
        # 1. greate file handler object
        # 2. read the images from the file using file handler object
        # 3. add images to image manager object's image list to process them
        self.file_handlerer = FileHandler("images.json")
        images = self.file_handlerer.read()
        for image in images:
            self.image_manager.add_image_to_image_list(image)

    def print_image_list(self):
        # 1. get images from image manager object
        # 2. print images
        images = self.image_manager.return_images()
        for image in images:
            print(image)

    def find_image(self):
        # 1. get id from user
        # 2. get image from image manager object
        # 3. print image
        id = int(input("Enter image id: "))
        image = self.image_manager.return_image(id)
        if image:
            print(image)
        else:
            print("Image not found")

    def run(self):
        self.load_images()

        while True:
            print("1. Print image list")
            print("2. Find image")
            print("3. Exit")
            choice = input("Enter your choice: ")
            if choice == "1":
                self.print_image_list()
            elif choice == "2":
                self.find_image()
            elif choice == "3":
                break
            else:
                print("Invalid choice")


if __name__ == "__main__":
    app = ImageManagerApp().run()
    #images = FileHandler("images.json").read()
    #print(images)