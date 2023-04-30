from PIL import Image
from entities.image_object import ImageObject
from repositories.database_repository import DatabaseRepository
from config import IMAGE_FILES_PATH

# The metadata and imge files are loaded from the disk and database and
# returned as an ImageObject, which are stored in a list.
# The manipulation of the ImageObjects are done in the ImageManager class and
# the changes are stored to disk/database only when the user saves the changes.
# Thats why it not necessary to for examplme excetute searches from the database.


class ImageManager:
    def __init__(self):
        # list to store image objects
        self.image_list = []
        self.data_base = DatabaseRepository()

    def test_db_load(self):
        self.data_base.init_db_from_json()

    def open_image(self, image_path):
        # open image from disk
        return Image.open(image_path)

    def load_image_from_file(self, image_paths):
        """gets a list of image paths and returns a list of image objects"""
        image_objects = []
        # load image from disk
        for path in image_paths:
            image = self.open_image(path)
            # get image name from path
            image_name = path.split("/")[-1]
            # create image object
            image_objects.append(ImageObject(None, image_name, [], image))
        # return image object
        return image_objects

    def load_image_data_from_database(self):
        # load image data from database
        image_data = self.data_base.get_all_image_data()
        for image in image_data:
            image_id = image["id"]
            image_name = image["file_name"]
            image_tags = image["tags"].split(",")
            image_path = IMAGE_FILES_PATH + image_name
            image_picture = self.open_image(image_path)
            self.image_list.append(ImageObject(
                image_id, image_name, image_tags, image_picture))

    def get_all_images(self):
        return self.image_list

    def search_for_tag(self, tag):
        # return list of image objects
        image_list = [image for image in self.image_list if tag in image.tags]

        if image_list:
            return image_list
        return None

    def add_tag(self, image, tag):
        tag = tag.lower()
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

    def tag_statistics(self):
        # returns a dictionary with all tags and their count
        tag_statistics = {}
        tag_data = [row["tags"].split(',')
                    for row in self.data_base.get_all_tags()]

        for tag_row in tag_data:
            for tag in tag_row:
                if tag in tag_statistics:
                    tag_statistics[tag] += 1
                else:
                    tag_statistics[tag] = 1

        # sort the dictionary by tag count
        return dict(sorted(tag_statistics.items(), key=lambda x: x[1]))

    def save_tag_changes(self, image_list):
        # saves the tag updates to the database if the user has
        # pressed the save button in the GUI's search or all images view
        for image in image_list:
            self.data_base.update_image_tags(image)

    def save_image(self, image_list):
        # new image metadata (name and tags) are saved to the database
        # and the image file is saved to disk, if the user has
        # pressed the save button in the GUI's add image view
        for image in image_list:
            self.data_base.add_image(image.name, ','.join(image.tags))
            image.picture.save(IMAGE_FILES_PATH + image.name)


image_manager = ImageManager()
