import json
from PIL import Image
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

    def open_image(self, image_path):
        """Avaa kuvatieodoston.

        Args:
            image_path (string): Polku kuvan sijaintiin.

        Returns:
            Image: Avattu kuva
        """
        return Image.open(image_path)

    def save_image(self, image_file, image_name):
        """Tallentaa kuvan levylle.

        Args:
            image_file (Image): Tallennettava kuva
            image_path (String): Polku kuvan tallennuspaikkaan
        """
        image_file.save(IMAGE_FILES_PATH + image_name)

    def get_list_of_images(self, image_paths):
        """Avaa kuvat polun perusteella ja palauttaa listan kuvista.

        Args:
            image_paths (list): Lista poluista kuvien sijaintiin.

        Returns:
            List: Lista Tupleja, joissa ensimmäinen alkio on kuvan nimi ja toinen kuva.
        """
        image_list = []
        for path in image_paths:
            image = self.open_image(path)
            image_name = path.split("/")[-1]
            image_list.append((image_name, image))
        return image_list


file_repository = FileRepository()
