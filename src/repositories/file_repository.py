import json
from PIL import Image
from config import IMAGE_FILES_PATH, IMAGE_METADATA_PATH


class FileRepository:
    """Luokka vastaa tiedostojen käsittelystä.
    """

    def __init__(self,
                 file_path=IMAGE_FILES_PATH,
                 conf_path=IMAGE_METADATA_PATH):
        self.file_path = file_path
        self.conf_path = conf_path
        """Konstruktori, joka luo olion kuvatietojen sekä metadata-tiedostojen tallenuspaikasta.

        Args:
            file_path (String): Polku kuvien tallennuspaikkaan.
            conf_path (String): Polku kuvien metadata-tiedostoon. 
        """

    def read_conf_file(self):
        """Lukee kuvien metadata-tiedoston, joka pitää sisällään tietoja kuvien nimistä ja tageista,
          ja palauttaa sen sisällön.

        Returns:
            List: Lista kuvien tiedoista.
        """
        try:
            with open(self.conf_path, 'r', encoding='utf8') as file:
                return json.load(file)
        except FileNotFoundError:
            print(f"File {self.conf_path} not found")
            return None

    def write_conf_file(self, data):
        """Kirjoittaa kuvien metadata-tiedoston levylle, 
        joka pitää sisällään tietoja kuvien nimistä ja tageista.
        """
        try:
            dicts = [{"name": image.name, "tags": image.tags}
                     for image in data]
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
        """Avaa kuvat polun perusteella ja palauttaa kuvan nimen ja kuvan.

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
