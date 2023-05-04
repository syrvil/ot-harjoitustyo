import unittest
from repositories.image_repository import image_repository
from entities.image_object import ImageObject

class TestImageRepository(unittest.TestCase):
    def setUp(self):
        self.test_image = ImageObject(1, "test_image.jpg", ["tag3", "tag4"], None)
    
    def test_add_image_data(self):
        image_repository.add_image_data("test_image.jpg", "tag1,tag2")
        result = image_repository.get_all_image_data()
        self.assertEqual(result[0][1], "test_image.jpg")
    
    def test_get_all_image_data(self):
        image_repository.add_image_data("test_image2.jpg", "tag5,tag6")
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
        self.assertEqual(result[0]["tags"], "tag1,tag2")
        self.assertEqual(result[1]["tags"], "tag5,tag6")