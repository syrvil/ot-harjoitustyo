class Id:
    id = 0

    @classmethod
    def next_id(cls):
        cls.id += 1  # or Id.id += 1
        return cls.id  # return Id.id


class ImageObject:
    def __init__(self, name, tags):
        self.name = name
        self.tags = tags
        Id.next_id()
        self.id = Id.id

    def __str__(self):
        return f"[{self.id}] name: {self.name}, tags: {self.tags}"
