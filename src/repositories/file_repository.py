import json
# from entities.image_object import ImageObject
from config import IMAGE_MEDATA_PATH


class FileRepository:
    """Class handling image file operations"""

    def __init__(self, filename=IMAGE_MEDATA_PATH):
        self.filename = filename

    def read_file(self):
        """Reads image data from file"""
        try:
            with open(self.filename, 'r', encoding='utf8') as file:
                return json.load(file)
        except FileNotFoundError:
            print(f"File {self.filename} not found")

    def write_file(self, data):
        """Writes image data to file"""
        # convert image objects to list of dictionaries
        dicts = [{"name": image.name, "tags": image.tags} for image in data]
        # add: write imgage-file to disk
        with open(self.filename, 'w', encoding='utf8') as file:
            json.dump(dicts, file, indent=4)
