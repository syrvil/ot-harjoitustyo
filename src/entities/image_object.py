class ImageObject:
    def __init__(self, name, tags, picture):
        self.name = name
        self.tags = tags
        self.picture = picture

    def __str__(self):
        return f"name: {self.name}, tags: {self.tags}"
