class ImageObject:
    def __init__(self, id, name, tags, picture):
        self.id = id
        self.name = name
        self.tags = tags
        self.picture = picture

    def __str__(self):
        return f"id: {self.id}, name: {self.name}, tags: {self.tags}"
