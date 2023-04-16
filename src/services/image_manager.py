from PIL import Image
from entities.image_object import ImageObject
from repositories.file_repository import FileRepository
from config import IMAGE_FILES_PATH


class ImageManager:
    def __init__(self):
        # list to store image objects
        self.image_list = []

    def load_images_from_file(self):
        # load image metadata from json-file:
        # file-name and tags
        imgs = FileRepository().read_file()
        for image in imgs:
            self.add_image_to_list(image)

    def __open_image(self, image_path):
        # open image from disk
        return Image.open(image_path)

    def add_image_to_list(self, image_data, image_picture=None):
        # add imgage to image list as an Image object
        image_name = image_data["name"]
        # convert tags to lower case
        image_tags = [tag.lower() for tag in image_data["tags"]]
        if not image_picture:
            image_path = IMAGE_FILES_PATH + image_name
            image_picture = self.__open_image(image_path)
        self.image_list.append(ImageObject(
            image_name, image_tags, image_picture))

    def get_all_images(self):
        return self.image_list

    def search_for_tag(self, tag):
        # return list of image objects
        image_list = [image for image in self.image_list if tag in image.tags]

        if image_list:
            return image_list
        return None

    def add_tag(self, image, tag):
        # add tag to image
        if tag not in image.tags:
            image.tags.append(tag)
            return True
        return False

    def delete_tag(self, image, tag):
        # delete tag from image
        if tag in image.tags:
            image.tags.remove(tag)
            return True
        return False


image_manager = ImageManager()
