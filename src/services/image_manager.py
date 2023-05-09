from entities.image_object import ImageObject
from repositories.image_repository import image_repository
from repositories.file_repository import file_repository
from config import IMAGE_FILES_PATH


class ImageManager:
    """Luokka, joka vastaa kuvien käsittelystä.
    """

    def __init__(self,
                 data_base=image_repository,
                 image_files=file_repository):
        """Konstruktori, joka luo käsittelystä vastvaan olion jossa ImangeObject-oliot
        tallennetaan listaan käsittelyä varten sekä olion, jolla ImageObect olioiden 
        dataa voidaan käsitellä tietotokannassa. 
        """
        self.image_list = []
        self.data_base = data_base
        self.image_files = image_files

    def load_json_to_db(self):
        """Lataa JSON-muodossa olevan metadatatiedon tietokantaan.
        """
        self.data_base.init_db_from_json()

    def load_image_from_file(self, image_paths):
        """Avaa kuvat anneutusta sijainnista ja luo niistä ImageObject oliot.
        Kuvilla ei vielä ole id:tä eikä tageja. Nimi on tiedoston nimi.

        Args:
            image_paths (list): Lista poluista kuvien sijaintiin.

        Returns:
            List: Lista ImageObject-oloista
        """

        images = self.image_files.get_list_of_images(image_paths)

        image_objects = []
        for image in images:
            image_objects.append(ImageObject(None, image[0], [], image[1]))
        return image_objects

    def load_repository_data(self):
        """Lataa image- ja filerepositorioissa olevan datan kaikista kuvista. 
        Datan perusteella kuvista luodaan lista ImageObejct-olioita, 
        jotka tallennetaan luokan muuttujaan.
        """
        image_data = self.data_base.get_all_image_data()
        for image in image_data:
            image_id = image["id"]
            image_name = image["file_name"]
            image_tags = image["tags"].split(",")
            image_path = IMAGE_FILES_PATH + image_name
            image_picture = self.image_files.open_image(image_path)
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
        image_list = [
            image for image in self.image_list if tag.lower() in image.tags]

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
        if tag.lower() not in image.tags:
            image.tags.append(tag.lower())
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
        if tag.lower() in image.tags:
            image.tags.remove(tag.lower())
            return True
        return False

    def tag_statistics(self):
        """Laskee kuinka monta eri nimistä tagia ImageObject olioilla on. 

        Returns:
            Dictionary: Tagien määrän mukaan järjestetty sanakirja.
        """
        tag_statistics = {}

        for tag_row in self.data_base.get_all_tags():
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
            self.data_base.add_image_data(image.name, image.tags)
            self.image_files.save_image(image.picture, image.name)


image_manager = ImageManager()
