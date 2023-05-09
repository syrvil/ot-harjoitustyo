from database_connection import get_database_connection


def drop_tables(connection):
    """Poistaa tietokannasta kaikki taulut.

    Args: Tietokantayhteys
    """
    cursor = connection.cursor()

    cursor.execute("""
        drop table if exists images;
    """)

    connection.commit()


def create_tables(connection):
    """Luo tietokantaan tarvittavat taulut.

    Args: Tietokantayhteys
    """
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
    """Alustaa tietokannan poistmalla ja luomalla tarvittavat taulut.
    """
    connection = get_database_connection()

    drop_tables(connection)
    create_tables(connection)
