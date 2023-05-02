from PIL import Image
from entities.image_object import ImageObject
from repositories.image_repository import image_repository
from config import IMAGE_FILES_PATH


class ImageManager:
    """Luokka, joka vastaa kuvien käsittelystä.
    """

    def __init__(self):
        """Konstruktori, joka luo käsittelystä vastvaan olion jossa ImangeObject-oliot
        tallennetaan listaan käsittelyä varten sekä olion, jolla ImageObect olioiden 
        dataa voidaan käsitellä tietotokannassa. 
        """
        self.image_list = []
        self.data_base = image_repository

    def test_db_load(self):
        """Lataa JSON-muodossa olevan metadatatiedon tietokantaan.
        """
        self.data_base.init_db_from_json()

    def open_image(self, image_path):
        """Avaa kuvatieodoston.

        Args:
            image_path (string): Polku kuvan sijaintiin.

        Returns:
            Image: Avattu kuva
        """
        return Image.open(image_path)

    def load_image_from_file(self, image_paths):
        """Avaa kuvat jotka eivät ole tietokannassa ja luo niistä ImageObject oliot.
        Kuvilla ei vielä ole id:tä eikä tageja. Nimi on tiedoston nimi.

        Args:
            image_paths (list): Lista poluista kuvien sijaintiin.

        Returns:
            List: Lista ImageObject-oloista
        """
        image_objects = []
        for path in image_paths:
            image = self.open_image(path)
            image_name = path.split("/")[-1]
            image_objects.append(ImageObject(None, image_name, [], image))
        return image_objects

    def load_image_data_from_database(self):
        """Lataa tietokannassa olevan datan kaikista kuvista. Kuvan nimen sekä 
        kuvahakemiston polun avulla avaa kuvan. Tietojen perusteella kuvista luodaan
        lista ImageObejct-olioita jotka tallennetaan luokan muuttujaan.
        """
        image_data = self.data_base.get_all_image_data()
        for image in image_data:
            image_id = image["id"]
            image_name = image["file_name"]
            image_tags = image["tags"].split(",")
            image_path = IMAGE_FILES_PATH + image_name
            image_picture = self.open_image(image_path)
            self.image_list.append(ImageObject(
                image_id, image_name, image_tags, image_picture))

    def get_all_images(self):
        """Palauttaa luokkaan säilötyt ImageObject oliot.

        Returns:
            List: Lista ImageObject-olioista
        """
        return self.image_list

    def search_for_tag(self, tag):
        """Etsii tagin perusteella ImageObject-olioita.

        Args:
            tag (string): Etsittävä tagi.

        Returns:
            List: Lista ImageObject olioita, joilla annettu tagi. 
        """
        image_list = [image for image in self.image_list if tag in image.tags]

        if image_list:
            return image_list
        return None

    def add_tag(self, image, tag):
        """Lisää tagin ImageObject oliolle. Tagi muutetaan pienellä kirjoitetetuksi
        ennen lisäystä.

        Args:
            image (ImageObect): Olio, jolle tagi lisätään.
            tag (String): Lisättävä tagi.

        Returns:
            Boolean: True, jos oliolle ei ollut entuudestaan kyseistä tagia. 
        """
        tag = tag.lower()
        if tag not in image.tags:
            image.tags.append(tag)
            return True
        return False

    def delete_tag(self, image, tag):
        """Poistaa tagin ImageObject oliolta.

        Args:
            image (ImageObejct): Olio, jolta tagi poistetaan.
            tag (String): Poistettava tagi.

        Returns:
            Boolean: True, jos oliolla oli kyseinen tagi.
        """
        if tag in image.tags:
            image.tags.remove(tag)
            return True
        return False

    def tag_statistics(self):
        """Laskee kuinka monta eri nimistä tagia ImageObject olioilla on. 

        Returns:
            Dictionary: Tagien määrän mukaan järjestetty sanakirja.
        """
        tag_statistics = {}
        tag_data = [row["tags"].split(',')
                    for row in self.data_base.get_all_tags()]

        for tag_row in tag_data:
            for tag in tag_row:
                if tag in tag_statistics:
                    tag_statistics[tag] += 1
                else:
                    tag_statistics[tag] = 1

        return dict(sorted(tag_statistics.items(), key=lambda x: x[1]))

    def save_tag_changes(self, image_list):
        """Päivittää ImageObject olioiden tagit tietokantaan.

        Args:
            image_list (List): Lista olioista.
        """
        for image in image_list:
            self.data_base.update_image_tags(image)

    def save_image(self, image_list):
        """Lisää ImageObject olion (tiedosto)nimen ja tagit tietokantaan, 
        ja tallentaa kuvan kuvahakemistoon. 

        Args:
            image_list (List): Lista olioista.
        """
        for image in image_list:
            self.data_base.add_image_data(image.name, ','.join(image.tags))
            image.picture.save(IMAGE_FILES_PATH + image.name)


image_manager = ImageManager()
