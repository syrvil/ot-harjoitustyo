import unittest
from mockup import Image

class TestImage(unittest.TestCase):
    def setUp(self):
        pass
    
    def test_image_name(self):
        image = Image("test", [])
        self.assertEqual(image.name, "test")

    def test_image_tags(self):
        image = Image("test", [])
        self.assertEqual(image.tags, [])

    def test_image_str(self):
        image = Image("test", [])
        self.assertEqual(str(image), "name: test tags: []")