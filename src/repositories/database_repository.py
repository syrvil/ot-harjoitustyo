import sqlite3
from repositories.file_repository import FileRepository
from config import DATABASE_FILE_PATH

connection = sqlite3.connect(DATABASE_FILE_PATH)
connection.row_factory = sqlite3.Row


def get_database_connection():
    return connection


### database initialization functions
def drop_tables(connection):
    cursor = connection.cursor()

    cursor.execute("""
        drop table if exists images;
    """)

    connection.commit()


def create_tables(connection):
    cursor = connection.cursor()

    cursor.execute("""
        create table images (
            id integer primary key autoincrement,
            file_name text,
            tags text
        );
    """)

    connection.commit()


def initialize_database():
    connection = get_database_connection()

    drop_tables(connection)
    create_tables(connection)


class DatabaseRepository:
    def __init__(self):
        initialize_database()
        self.connection = get_database_connection()

    def _list_to_string(self, list):
        return ','.join(list)

    def init_db_from_json(self):
        # loads image metadata from json-file and stores it to database
        json_data = FileRepository().read_conf_file()
        for image_data in json_data:
            image_name = image_data["name"]
            # make a string of of a list of tags
            image_tags = self._list_to_string(image_data["tags"])
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
        """, (self._list_to_string(image.tags), image.id))
        self.connection.commit()
