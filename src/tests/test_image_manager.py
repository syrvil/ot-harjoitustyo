import unittest
import io
from io import BytesIO
from PIL import Image
from entities.image_object import ImageObject
from services.image_manager import ImageManager

TEST_IMAGE = Image.new('RGB', (128, 128))
with io.BytesIO() as buffer:
    TEST_IMAGE.save(buffer, format='JPEG')
    IMAGE_DATA = buffer.getvalue()


class DbFileStub:
    """Tynkäluokka (valekomponennti), joka simuloi tietokanta- ja tiedosto-operaatioita."""

    def __init__(self):
        self.image_name = "image1.jpg"
        self.image_data = Image.open(BytesIO(IMAGE_DATA))
        self.image_list = []

    def get_list_of_images(self, image_paths):
        image_list = []
        for _ in image_paths:
            image_list.append((self.image_name, self.image_data))
        return image_list

    def get_all_tags(self):
        return [["tag1", "tag2"], ["tag2", "tag4"]]

    def get_all_image_data(self):
        return [{"id": 3, "file_name": "image3.jpg", "tags": "tag5,tag6"},
                {"id": 4, "file_name": "image4.jpg", "tags": "tag7,tag8"}]

    def open_image(self, image_path):
        if image_path:  # pylint hack
            image = self.image_data
        else:
            image = self.image_data
        return image


class TestImageManager(unittest.TestCase):
    def setUp(self):
        test_image = Image.open(BytesIO(IMAGE_DATA))
        self.test_list = [
            ImageObject(1, "image1.jpg", ["tag1", "tag2"], test_image),
            ImageObject(2, "image2.jpg", ["tag2", "tag4"], test_image),
        ]

        self.image_manager = ImageManager()
        self.image_manager.image_list = self.test_list
        self.test_source_data = [('image1.jpg', test_image)]
        self.tag_test_list = [["tag1", "tag2"], ["tag2", "tag4"]]

        self.stub_image_manager = ImageManager(data_base=DbFileStub(),
                                               image_files=DbFileStub())

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

    def test_search_for_tag_upper_case_found(self):
        result = self.image_manager.search_for_tag("TAG1")
        self.assertEqual(result[0].name, "image1.jpg")

    def test_search_for_tag_mixed_upper_case_found(self):
        result = self.image_manager.search_for_tag("tAg2")
        self.assertEqual(result[0].name, "image1.jpg")
        self.assertEqual(result[1].name, "image2.jpg")

    def test_add_tag_true(self):
        image = self.image_manager.get_all_images()[0]
        result = self.image_manager.add_tag(image, "new_tag")
        self.assertTrue(result)

    def test_add_tag_false(self):
        image = self.image_manager.get_all_images()[0]
        result = self.image_manager.add_tag(image, "tag1")
        self.assertFalse(result)

    def test_add_tag_upper_case_correct(self):
        image = self.image_manager.get_all_images()[0]
        self.image_manager.add_tag(image, "NEW_TAG")
        self.assertEqual(image.tags[2], "new_tag")

    def test_delete_tag_true(self):
        image = self.image_manager.get_all_images()[0]
        result = self.image_manager.delete_tag(image, "tag1")
        self.assertTrue(result)

    def test_delete_tag_false(self):
        image = self.image_manager.get_all_images()[0]
        result = self.image_manager.delete_tag(image, "tagataga3")
        self.assertFalse(result)

    def test_delete_tag_upper_case_correct(self):
        image = self.image_manager.get_all_images()[0]
        self.image_manager.delete_tag(image, "TAG1")
        self.assertEqual(image.tags, ["tag2"])

    def test_tag_statistics_correct(self):
        result = self.stub_image_manager.tag_statistics()
        self.assertDictEqual(result, {"tag1": 1, "tag2": 2, "tag4": 1})

    def test_tag_statistics_max_key_correct(self):
        result = self.stub_image_manager.tag_statistics()
        self.assertEqual(max(result, key=result.get), "tag2")

    def test_load_image_from_file_returns_objects(self):
        paths = ["path1", "path2"]
        images = self.stub_image_manager.load_image_from_file(paths)
        self.assertIsInstance(images[0], ImageObject)

    def test_load_image_from_file_returns_correct_number_of_objects(self):
        paths = ["path1", "path2"]
        images = self.stub_image_manager.load_image_from_file(paths)
        self.assertEqual(len(images), 2)

    def test_load_image_from_file_returns_correct_name(self):
        paths = ["path1", "path2"]
        images = self.stub_image_manager.load_image_from_file(paths)
        self.assertEqual(images[0].name, "image1.jpg")

    def test_load_image_from_file_returns_image_file(self):
        paths = ["path1", "path2"]
        images = self.stub_image_manager.load_image_from_file(paths)
        self.assertEqual(images[0].picture.size, (128, 128))

    def test_load_repository_data_returns_objects(self):
        self.stub_image_manager.load_repository_data()
        self.assertIsInstance(
            self.stub_image_manager.image_list[0], ImageObject)

    def test_load_repository_data_returns_correct_file(self):
        self.stub_image_manager.load_repository_data()
        self.assertEqual(
            self.stub_image_manager.image_list[0].name, "image3.jpg")

    def test_load_repository_data_returns_correct_tags(self):
        self.stub_image_manager.load_repository_data()
        self.assertListEqual(
            self.stub_image_manager.image_list[1].tags, ["tag7", "tag8"])
