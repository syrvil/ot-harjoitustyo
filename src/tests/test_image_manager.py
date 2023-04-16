import unittest
from PIL import Image
import io
from io import BytesIO 
from entities.image_object import ImageObject
from repositories.file_repository import FileRepository
from config import IMAGE_FILES_PATH
from services.image_manager import ImageManager

TEST_IMAGE = Image.new('RGB', (128, 128))
with io.BytesIO() as buffer:
    TEST_IMAGE.save(buffer, format='JPEG')
    image_data = buffer.getvalue()

class TestImageManager(unittest.TestCase):
    def setUp(self):
        # create a mock JPEG image
        #image_data = b'\xff\xd8\xff\xe0\x00\x10JFIF\x00\x01\x01\x00\x00\x01\x00\x01\x00\x00\xff\xdb\x00\x84...'
  
        # create test image
        test_image = Image.open(BytesIO(image_data))
        # generate test data
        self.test_list = [
            ImageObject("image1.jpg", ["tag1", "tag2"], test_image),
            ImageObject("image2.jpg", ["tag2", "tag4"], test_image),
        ]

        # create a new image manager
        self.image_manager = ImageManager()
        self.image_manager.image_list = self.test_list
    
    #def test_add_image_to_list(self):
        # create a new mock image
        #image_data = b'\xff\xd8\xff\xe0\x00\x10JFIF\x00\x01\x01\x00\x00\x01\x00\x01\x00\x00\xff\xdb\x00\x84...'
    #    mock_image = Image.open(BytesIO(image_data))

        # add the mock image to the image list
    #    self.image_manager.add_image_to_list({"name": "image3.jpg", "tags": ["tag3", "tag4"], "picture": mock_image})

        # check if the image was added to the list
    #    self.assertEqual(len(self.image_manager.get_all_images()), 3)

    def test_get_all_images(self):
        # check if the correct number of images were loaded
        self.assertEqual(len(self.image_manager.get_all_images()), 2)

        # check if the correct images were loaded
        #self.assertEqual(self.image_manager.get_all_images()[0].name, "image1.jpg")
        #self.assertEqual(self.image_manager.get_all_images()[1].name, "image2.jpg")

    def test_search_for_tag(self):
        # search for images with tag "tag2"
        result = self.image_manager.search_for_tag("tag2")

        # check if the correct number of images were found
        self.assertEqual(len(result), 2)

        # check if the correct images were found
        self.assertEqual(result[0].name, "image1.jpg")
        self.assertEqual(result[1].name, "image2.jpg")
    
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
