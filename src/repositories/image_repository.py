from database_connection import get_database_connection
from initialize_database import initialize_database
from repositories.file_repository import file_repository


class ImageRepository:
    """Luokka ImageObject datan tietokantaoperaatioita varten
    """

    def __init__(self, connection):
        """Konstruktori, joka alustaa tietokannan ja muodostaa tietokantayhteyden.

        Args:
            connection (Connection): Tietokannan yhteysolio.
        """
        initialize_database()
        self.connection = connection

    def __list_to_string(self, tag_list):
        """Apufunktio, joka muodostaa listasta merkkijonon tietokantatannusta varten.

        Args:
            tag_list (List): Lista tageista.

        Returns:
            String: Merkkijono, jossa tagit on eroteltu pilkulla.
        """
        return ','.join(tag_list)

    def init_db_from_json(self):
        """Lukee json-muodossa olevan datan ja tallentaa sen tietokantaan.
        """
        json_data = file_repository.read_conf_file()
        for image_data in json_data:
            image_name = image_data["name"]
            image_tags = self.__list_to_string(image_data["tags"])
            self.add_image_data(image_name, image_tags)

    def add_image_data(self, name, tags):
        """Lisää kuvan tiedot tietokantaan.

        Args:
            name (String): Kuvan tidostonimi
            tags (String): Kuvan tagit pilkulla eroteltuna.
        """
        cursor = self.connection.cursor()
        cursor.execute("""
            insert into images (file_name, tags)
            values (?, ?)
        """, (name, tags))
        self.connection.commit()

    def get_all_image_data(self):
        """Hakee kaiken kuvadatan tietokannasta.
        
        Returns:
            Cursor: Tietokannasta haettu data.
        """
        cursor = self.connection.cursor()
        cursor.execute("""
            select * from images
        """)
        return cursor.fetchall()

    def update_image_tags(self, image):
        """Päivittää kuvan tagit tietokantaan.

        Args:
            image (ImageObject): Kuva, jonka tagit päivitetään.
        """
        cursor = self.connection.cursor()
        cursor.execute("""
            update images set tags = ?
            where id = ?
        """, (self.__list_to_string(image.tags), image.id))
        self.connection.commit()

    def get_all_tags(self):
        """Hakee kaikki tagit tietokannasta.

        Returns:
            Cursor: Tietokannasta haettu data.
        """
        cursor = self.connection.cursor()
        cursor.execute("""
            select tags from images
        """)
        return cursor.fetchall()


image_repository = ImageRepository(get_database_connection())
