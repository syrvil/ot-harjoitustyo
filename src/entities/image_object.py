class ImageObject:
    def __init__(self, image_id, name, tags, picture):
        self.id = image_id
        self.name = name
        self.tags = tags
        self.picture = picture
        self.__tags_to_lowercase()

    def __tags_to_lowercase(self):
        self.tags = [tag.lower() for tag in self.tags]


    def __str__(self):
        return f"id: {self.id}, name: {self.name}, tags: {self.tags}"
