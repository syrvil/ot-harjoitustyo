from database_connection import get_database_connection
from initialize_database import initialize_database
from repositories.file_repository import FileRepository

class DatabaseRepository:
    def __init__(self, connection):
        initialize_database()
        self.connection = connection

    def __list_to_string(self, tag_list):
        return ','.join(tag_list)

    def init_db_from_json(self):
        # loads image metadata from json-file and stores it to database
        json_data = FileRepository().read_conf_file()
        for image_data in json_data:
            image_name = image_data["name"]
            # make a string of of a list of tags
            image_tags = self.__list_to_string(image_data["tags"])
            self.add_image(image_name, image_tags)

    def add_image(self, name, tags):
        cursor = self.connection.cursor()
        cursor.execute("""
            insert into images (file_name, tags)
            values (?, ?)
        """, (name, tags))
        self.connection.commit()

    def get_all_image_data(self):
        cursor = self.connection.cursor()
        cursor.execute("""
            select * from images
        """)
        return cursor.fetchall()

    def update_image_tags(self, image):
        cursor = self.connection.cursor()
        cursor.execute("""
            update images set tags = ?
            where id = ?
        """, (self.__list_to_string(image.tags), image.id))
        self.connection.commit()

    def get_all_tags(self):
        cursor = self.connection.cursor()
        cursor.execute("""
            select tags from images
        """)
        return cursor.fetchall()

image_repository = DatabaseRepository(get_database_connection())