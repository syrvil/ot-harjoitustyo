import unittest
from mockup import Id, Image, ImageManager

class TestId(unittest.TestCase):
    def test_next_id(self): 
        cls = Id()
        self.assertEqual(cls.next_id(), 1)

class TestImage(unittest.TestCase):
    def setUp(self):
        self.image = Image("test", ["tag1", "tag2"])
    
    def test_image_name(self):
        self.assertEqual(self.image.name, "test")

    def test_image_tags(self):
        self.assertEqual(self.image.tags, ["tag1", "tag2"])

    def test_image_id(self):
        self.assertEqual(self.image.id, 2)

    def test_image_str(self):
        self.assertEqual(str(self.image), "[4] name: test, tags: ['tag1', 'tag2']")

class TestImageManager(unittest.TestCase):
    def setUp(self):
        self.image = Image("test", ["tag1", "tag2"])
        self.image_manager = ImageManager()
        self.image_manager.image_list = [self.image]

    def test_add_image_to_list(self):
        self.image_manager.add_image_to_list({"name": "test2", "tags": ["tag3", "tag4"]})
        self.assertEqual(self.image_manager.image_list[1].name, "test2")

    def test_return_image_id_exists(self):
        self.assertEqual(self.image_manager.return_image(self.image.id), self.image)

    def test_return_image_id_does_not_exist(self):
        self.assertEqual(self.image_manager.return_image(100), None)

    def test_return_all_images(self):
        self.assertEqual(self.image_manager.return_all_images(), [self.image])

    def test_images_with_tag(self):
        self.assertEqual(self.image_manager.images_with_tag("tag1"), [self.image])

    def test_images_with_tag_does_not_exist(self):
        self.assertEqual(self.image_manager.images_with_tag("tag3"), None)

    def test_add_tag(self):
        self.assertEqual(self.image_manager.add_tag(self.image.id, "tag3"), self.image)

    def test_add_tag_tag_exists(self):
        self.assertRaises(Exception, self.image_manager.add_tag, self.image.id, "tag1")

    def test_add_tag_image_does_not_exist(self):
        self.assertRaises(Exception, self.image_manager.add_tag, 100, "tag1")

    def test_delete_tag(self):
        self.assertEqual(self.image_manager.delete_tag(self.image.id, "tag1"), self.image)

    def test_delete_tag_tag_does_not_exist(self):
        self.assertRaises(Exception, self.image_manager.delete_tag, self.image.id, "tag3")

    def test_delete_tag_image_does_not_exist(self):
        self.assertRaises(Exception, self.image_manager.delete_tag, 100, "tag1")
    