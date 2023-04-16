import unittest
from PIL import Image
import io
from io import BytesIO 
from entities.image_object import ImageObject
from repositories.file_repository import FileRepository
from services.image_manager import ImageManager

TEST_IMAGE = Image.new('RGB', (128, 128))
with io.BytesIO() as buffer:
    TEST_IMAGE.save(buffer, format='JPEG')
    IMAGE_DATA = buffer.getvalue()

class TestImageManager(unittest.TestCase):
    def setUp(self):
        # create a test image
        test_image = Image.open(BytesIO(IMAGE_DATA))
        # generate test data
        self.test_list = [
            ImageObject("image1.jpg", ["tag1", "tag2"], test_image),
            ImageObject("image2.jpg", ["tag2", "tag4"], test_image),
        ]

        # create a new image manager
        self.image_manager = ImageManager()
        # add the test data to the image manager
        self.image_manager.image_list = self.test_list
    
    def test_add_image_to_list(self):
        test_image = Image.open(BytesIO(IMAGE_DATA))
        self.image_manager.add_image_to_list(
            {"name": "image3.jpg", "tags": ["tag5", "tag6"]}, test_image)

        # check if the image was added to the list
        self.assertEqual(len(self.image_manager.get_all_images()), 3)

    def test_get_all_images_number_correct(self):
        # check if the correct number of images were loaded
        self.assertEqual(len(self.image_manager.get_all_images()), 2)

    def test_get_all_images_correct_image(self):
        # check if the correct images were loaded
        self.assertEqual(self.image_manager.get_all_images()[1].name, "image2.jpg")

    def test_search_for_tag_found(self):
        # search for images with tag "tag2"
        result = self.image_manager.search_for_tag("tag2")
        self.assertIsNotNone(result)

    def test_search_for_tag_not_found(self):
        # search for images with tag "tagataga3"
        result = self.image_manager.search_for_tag("tagataga3")

        # check if no images were found
        self.assertIsNone(result)

    def test_add_tag(self):
        # get the first image from the image list
        image = self.image_manager.get_all_images()[0]

        # add a new tag to the image
        result = self.image_manager.add_tag(image, "new_tag")

        # check if the tag was added to the image
        self.assertTrue(result)
        self.assertIn("new_tag", image.tags)

    def test_delete_tag(self):
        # get the first image from the image list
        image = self.image_manager.get_all_images()[0]

        # delete an existing tag from the image
        result = self.image_manager.delete_tag(image, "tag1")

        # check if the tag was deleted from the image
        self.assertTrue(result)
        self.assertNotIn("tag1", image.tags)
