import unittest
from repositories.image_repository import image_repository
from entities.image_object import ImageObject


class TestImageRepository(unittest.TestCase):
    """Luokka vastaa ImageRepository-luokan tietokantafunktioiden testaamisesta.
    Tyjä testitietokanta alustetaan kun luokka importoidaan, joten sitä ei tarvitse 
    luoda erikseen setUp metodissa."""

    def setUp(self):
        self.test_image = ImageObject(
            1, "test_image_1.jpg", ["tag3", "tag4"], None)

    def test_add_image_data_name_correct(self):
        image_repository.add_image_data(
            self.test_image.name, self.test_image.tags)
        result = image_repository.get_all_image_data()
        self.assertEqual(result[0][1], "test_image_1.jpg")

    def test_add_image_data_tags_correct(self):
        result = image_repository.get_all_image_data()
        self.assertEqual(result[0][2], "tag3,tag4")

    def test_get_all_image_data_len_correct(self):
        image_repository.add_image_data("test_image_2.jpg", ["tag5,tag2"])
        result = image_repository.get_all_image_data()
        self.assertEqual(len(result), 2)

    def test_update_image_tags(self):
        image_repository.update_image_tags(self.test_image)
        result = image_repository.get_all_image_data()
        self.assertEqual(result[0][2], "tag3,tag4")

    def test_get_all_tags_len_right(self):
        result = image_repository.get_all_tags()
        self.assertEqual(len(result), 2)

    def test_get_all_tags_right(self):
        result = image_repository.get_all_tags()
        self.assertListEqual(result[0], ["tag3", "tag4"])
        self.assertListEqual(result[1], ["tag5", "tag2"])
