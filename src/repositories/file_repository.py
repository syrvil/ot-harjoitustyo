import json
from entities.image_object import ImageObject
from config import IMAGE_MEDATA_PATH

class FileRepository:
    """Class handling image file operations"""

    def __init__(self, filename=IMAGE_MEDATA_PATH):
        self.filename = filename

    def read_file(self):
        """Reads image data from file"""
        try:
            with open(self.filename, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            print(f"File {self.filename} not found")

    def write_file(self, data):
        """Writes image data to file"""
        # convert image objects to list of dictionaries
        dicts = [{"name": image.name, "tags": image.tags} for image in data]
        # dicts = [image.__dict__ for image in data]
        with open(self.filename, 'w') as f:
            json.dump(dicts, f, indent=4)

    def read_images(self):
        """Reads image data from file and returns list of Image objects"""
        image_list = []
        for image in self.read_file():
            image_name = image["name"]
            # convert tags to lower case
            image_tags = [tag.lower() for tag in image["tags"]]
            image_list.append(ImageObject(image_name, image_tags))
        return image_list
