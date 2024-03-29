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

    def init_db_from_json(self):
        """Lukee json-muodossa olevan datan ja tallentaa sen tietokantaan.
        """
        json_data = file_repository.read_conf_file()
        for image_data in json_data:
            image_name = image_data["name"]
            image_tags = image_data["tags"]
            self.add_image_data(image_name, image_tags)

    def add_image_data(self, name, tags):
        """Lisää kuvan tiedostonimen ja tagit pilkuilla eroteltuna merkkijonona.

        Args:
            name (String): Kuvan tidostonimi.
            tags (List): Kuvan tagit.
        """
        cursor = self.connection.cursor()
        cursor.execute("""
            insert into images (file_name, tags)
            values (?, ?)
        """, (name, ','.join(tags)))
        self.connection.commit()

    def get_all_image_data(self):
        """Hakee kaiken kuvadatan tietokannasta.

        Returns:
            Cursor: Tietokannasta haettu dataolio, jossa kaikki tietokannan data.
        """
        cursor = self.connection.cursor()
        cursor.execute("""
            select * from images
        """)
        return cursor.fetchall()

    def update_image_tags(self, image):
        """Päivittää kuvan tagit tietokantaan merkkijonona, 
        jossa tagit eroteltu pilkulla.

        Args:
            image (ImageObject): Kuva, jonka tagit päivitetään.
        """
        cursor = self.connection.cursor()
        cursor.execute("""
            update images set tags = ?
            where id = ?
        """, (','.join(image.tags), image.id))
        self.connection.commit()

    def get_all_tags(self):
        """Hakee kaikki tagit tietokannasta.

        Returns:
            List: Lista, jossa lista jokaisen kuvan tageista.
        """
        cursor = self.connection.cursor()
        cursor.execute("""
            select tags from images
        """)
        rows = cursor.fetchall()
        return [row["tags"].split(',') for row in rows]


image_repository = ImageRepository(get_database_connection())
