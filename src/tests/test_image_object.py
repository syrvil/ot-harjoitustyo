import unittest
from entities.image_object import ImageObject

class TestImageObject(unittest.TestCase):
   
    def test_tags_to_lowercase_works_correct(self):
        test_image = ImageObject(1, "test_image_1.jpg", ["TAG1", "tAg2", "tag3"], None)
        self.assertListEqual(test_image.tags, ["tag1", "tag2", "tag3"])