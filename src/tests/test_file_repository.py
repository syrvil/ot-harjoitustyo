import unittest
from repositories.file_repository import file_repository
from config import SAMPLE_FILE_PATH


class TestFileRepository(unittest.TestCase):
    """Luokka vastaa FileRepository-luokan tiedostofunktioiden testaamisesta.
    Luokan olio, luodaan luokassa joten sitä ei tarvitse luoda erikseen setUp metodissa."""

    def setUp(self):
        self.file_path = SAMPLE_FILE_PATH + "im565.jpg"
        self.file_path2 = SAMPLE_FILE_PATH + "im565.jpg"
        self.file_paths = [self.file_path, self.file_path2]

    def test_open_image(self):
        image = file_repository.open_image(self.file_path)
        self.assertEqual(image.size, (128, 128))

    def test_get_list_of_images(self):
        image = file_repository.get_list_of_images(self.file_paths)
        self.assertEqual(image[0][0], "im565.jpg")
        self.assertEqual(image[1][0], "im565.jpg")

    def test_get_list_of_images_no_paths(self):
        image = file_repository.get_list_of_images([])
        self.assertEqual(image, [])
