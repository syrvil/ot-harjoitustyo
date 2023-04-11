import json
import sys
import os
from config import IMAGE_FILE_PATH, IMAGE_FILENAME

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
        return f"[{self.id}] name: {self.name}, tags: {self.tags}"

class Tags:
    pass

class FileHandler:
    def __init__(self, filename):
        #self.dirname = os.path.dirname(__file__) # __file__ is directory of this file
        #self.filename = os.path.join(IMAGE_FILE_PATH, filename)
        self.filename = filename

    def read_file(self):
        try:
            with open(self.filename, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            print(f"File {self.filename} not found")

    def write_file(self, data): 
        # convert image objects to list of dictionaries
        dicts = [{"name":image.name, "tags":image.tags} for image in data]   
        #dicts = [image.__dict__ for image in data]
        with open(self.filename, 'w') as f:
            json.dump(dicts, f, indent=4)

class ImageManager:
    def __init__(self):
        # list to store image objects
        self.image_list = []

    def add_image_to_list(self, image: dict):
        # add imgage to image list as an Image object
        image_name = image["name"]
        # convert tags to lower case
        image_tags = [tag.lower() for tag in image["tags"]]
        self.image_list.append(Image(image_name, image_tags))

    def return_image(self, id):
        # return image object
        for image in self.image_list:
            if image.id == id:
                return image
        return None
    
    def return_all_images(self):
        return self.image_list

    def images_with_tag(self, tag):
        # return list of image objects
        image_list = []
        for image in self.image_list:
            if tag in image.tags:
                image_list.append(image)
        if image_list:
            return image_list
        return None
    
    def add_tag(self, id, tag):
        # add tag to image
        image = self.return_image(id)
        if image:
            if tag not in image.tags:
                image.tags.append(tag)
                return image
            else:
                raise Exception("Tag already exists!")
        else:
            raise Exception("Image not found!")

    def delete_tag(self, id, tag):
        # delete tag from image
        image = self.return_image(id)
        if image:
            if tag in image.tags:
                image.tags.remove(tag)
                return image
            else:
                raise Exception("Tag does not exist!")
        else:
            raise Exception("Image not found!")


class ImageManagerApp:
    def __init__(self):
        # create an image manager object
        self.image_manager = ImageManager()
        self.file_handlerer = None

    def load_images(self):
        # 1. greate file handler object
        # 2. read the images from the file using file handler object
        # 3. add images to image manager object's image list to process them
        self.file_handlerer = FileHandler(IMAGE_FILE_PATH)
       
        print(f"Loading files from FILE:", IMAGE_FILENAME)
        print(f"Loading files from DIR:", IMAGE_FILE_PATH)
        
        images = self.file_handlerer.read_file()
        for image in images:
            self.image_manager.add_image_to_list(image)

    def print_image_list(self, images=None):
        # 1. get images from image manager object
        # 2. print images
        if not images:
            images = self.image_manager.return_all_images()
        for image in images:
            print(image)

    def find_image_with_id(self):
        # 1. get id from user
        # 2. get image from image manager object
        # 3. print image
        id = int(input("Enter image id: "))
        image = self.image_manager.return_image(id)
        if image:
            print(image)
        else:
            print("Image not found!")

    def find_images_with_tag(self):
        # 1. get tag from user
        # 2. get images from image manager object
        # 3. print images
        tag = input("Enter tag: ")
        images = self.image_manager.images_with_tag(tag.lower())
        if images:
            self.print_image_list(images)
        else:
            print("No images found!")

    def add_tag_to_image(self):
        # 1. get id from user
        # 2. get image from image manager object
        # 3. get tag from user
        # 4. add tag to image
        # 5. print image
        id = int(input("Enter image id: "))
        tag = input("Enter tag: ")
        try:
            self.image_manager.add_tag(id, tag.lower())
            print(f"Tag \"{tag}\" added successfully!")
        except Exception as e:
            print(e)

    def delete_tag_from_image(self):
        id = int(input("Enter image id: "))
        tag = input("Enter tag: ")
        try:
            self.image_manager.delete_tag(id, tag.lower())
            print(f"Tag \"{tag}\" DELETED successfully!")
        except Exception as e:
            print(e)

    def quit(self):
        # 1. get images from image manager object
        # 2. write images to file using file handler object
        save = input("Save changes? (y/n): ")
        if save == "y":
            images = self.image_manager.return_all_images()
            self.file_handlerer.write_file(images)
            print("Changes saved successfully!")
        else:
            print("Quitting without saving!")


    def run(self):
        self.load_images()

        while True:
            print("---------------------")
            print("Image Manager App 0.1")
            print("---------------------")
            print("1. Print image list")
            print("2. Find image with id")
            print("3. Find images with tag")
            print("4. Add tag to image")
            print("5. Delete tag from image")
            print("6. Exit")
            choice = input("Enter your choice: ")
            if choice == "1":
                self.print_image_list()
            elif choice == "2":
                self.find_image_with_id()
            elif choice == "3":
                self.find_images_with_tag()
            elif choice == "4":
                self.add_tag_to_image()
            elif choice == "5":
                 self.delete_tag_from_image()    
            elif choice == "6":
                self.quit()
                break
            else:
                print("Invalid choice")


if __name__ == "__main__":
    app = ImageManagerApp().run()
    #images = FileHandler("images.json").read_file()
    #print(images)