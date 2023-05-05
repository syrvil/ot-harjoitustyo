import json
# from entities.image_object import ImageObject
from config import IMAGE_FILES_PATH, IMAGE_METADATA_PATH


class FileRepository:
    """Class handling image file operations"""

    def __init__(self, 
                 file_path=IMAGE_FILES_PATH,
                 conf_path=IMAGE_METADATA_PATH):
        self.file_path = file_path
        self.conf_path = conf_path

    def read_conf_file(self):
        """Reads image data from file"""
        try:
            with open(self.conf_path, 'r', encoding='utf8') as file:
                return json.load(file)
        except FileNotFoundError:
            print(f"File {self.conf_path} not found")
            return None

    def write_conf_file(self, data):
        """Writes image data to file"""
        try:
            # convert image objects to list of dictionaries
            dicts = [{"name": image.name, "tags": image.tags}
                     for image in data]
            # add: write imgage-file to disk
            with open(self.file_path, 'w', encoding='utf8') as file:
                json.dump(dicts, file, indent=4)
        except FileNotFoundError:
            print(f"File {self.conf_path} not found")

file_repository = FileRepository()