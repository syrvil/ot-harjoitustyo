from entities.image_object import ImageObject
from repositories.file_repository import FileRepository


class ImageManager:
    def __init__(self):
        # list to store image objects
        self.image_list = []
        self.load_images()

    def load_images(self):
        # load images from file
        imgs = FileRepository().read_file()
        for image in imgs:
            self.add_image_to_list(image)

    def add_image_to_list(self, image: dict):
        # add imgage to image list as an Image object
        image_name = image["name"]
        # convert tags to lower case
        image_tags = [tag.lower() for tag in image["tags"]]
        self.image_list.append(ImageObject(image_name, image_tags))

    def return_image(self, id):
        # return image object
        for image in self.image_list:
            if image.id == id:
                return image
        return None

    def return_all_images(self):
        return self.image_list

    def images_with_tag(self, tag):
        # return list of image objects
        image_list = []
        for image in self.image_list:
            if tag in image.tags:
                image_list.append(image)
        if image_list:
            return image_list
        return None

    def add_tag(self, id, tag):
        # add tag to image
        image = self.return_image(id)
        if image:
            if tag not in image.tags:
                image.tags.append(tag)
                return image
            else:
                raise Exception("Tag already exists!")
        else:
            raise Exception("Image not found!")

    def delete_tag(self, id, tag):
        # delete tag from image
        image = self.return_image(id)
        if image:
            if tag in image.tags:
                image.tags.remove(tag)
                return image
            else:
                raise Exception("Tag does not exist!")
        else:
            raise Exception("Image not found!")


image_manager = ImageManager()
