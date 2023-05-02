import unittest
import io
from io import BytesIO
from PIL import Image
from entities.image_object import ImageObject
from services.image_manager import ImageManager
from config import SAMPLE_FILE_PATH

TEST_IMAGE = Image.new('RGB', (128, 128))
with io.BytesIO() as buffer:
    TEST_IMAGE.save(buffer, format='JPEG')
    IMAGE_DATA = buffer.getvalue()


class TestImageManager(unittest.TestCase):
    def setUp(self):
        test_image = Image.open(BytesIO(IMAGE_DATA))
        # generate test data
        self.test_list = [
            ImageObject(1, "image1.jpg", ["tag1", "tag2"], test_image),
            ImageObject(2, "image2.jpg", ["tag2", "tag4"], test_image),
        ]

        self.image_manager = ImageManager()
        self.image_manager.image_list = self.test_list

    def test_open_image(self):
        image = self.image_manager.open_image(SAMPLE_FILE_PATH+"im565.jpg")
        self.assertEqual(image.size, (128, 128))

    def test_load_image_from_file(self):
        image = self.image_manager.load_image_from_file(
            [SAMPLE_FILE_PATH+"im565.jpg"])
        self.assertEqual(image[0].name, "im565.jpg")

    def test_load_image_data_from_database(self):
        self.image_manager.load_image_data_from_database()
        self.assertEqual(len(self.image_manager.image_list), 2)

    def test_get_all_images_number_correct(self):
        self.assertEqual(len(self.image_manager.get_all_images()), 2)

    def test_get_all_images_correct_image(self):
        self.assertEqual(self.image_manager.get_all_images()
                         [1].name, "image2.jpg")

    def test_search_for_tag_found(self):
        result = self.image_manager.search_for_tag("tag2")
        self.assertIsNotNone(result)

    def test_search_for_tag_not_found(self):
        result = self.image_manager.search_for_tag("tagataga3")
        self.assertIsNone(result)

    def test_add_tag_true(self):
        image = self.image_manager.get_all_images()[0]
        result = self.image_manager.add_tag(image, "new_tag")
        self.assertTrue(result)

    def test_add_tag_false(self):
        image = self.image_manager.get_all_images()[0]
        result = self.image_manager.add_tag(image, "tag1")
        self.assertFalse(result)

    def test_delete_tag_true(self):
        image = self.image_manager.get_all_images()[0]
        result = self.image_manager.delete_tag(image, "tag1")
        self.assertTrue(result)

    def test_delete_tag_false(self):
        image = self.image_manager.get_all_images()[0]
        result = self.image_manager.delete_tag(image, "tagataga3")
        self.assertFalse(result)
