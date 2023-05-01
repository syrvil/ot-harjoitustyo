class ImageObject:
    """Luokka, joka kuvaa yksittäistä kuvaoliota
    """
    def __init__(self, image_id, name, tags, picture):
        """Luokan konstruktori, joka luo kuva-olion

        Args:
            image_id (int): kuvan yksilöllinen id
            name (string): kuvatiedoston nimi
            tags (list): lista taheista
            picture (Image): kuvaobjekti
        """
        self.id = image_id
        self.name = name
        self.tags = tags
        self.picture = picture
        self.__tags_to_lowercase()

    def __tags_to_lowercase(self):
        """Luokan sisäinen apufunktio, joka muuntaa tagit pieniksi kirjaimiksi
        """
        self.tags = [tag.lower() for tag in self.tags]

    def __str__(self):
        return f"id: {self.id}, name: {self.name}, tags: {self.tags}"
