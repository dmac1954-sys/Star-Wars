class Character:
    def __init__(
        self, name, key, url, description, species, home_world, gender, skin_color
    ):
        self.name = name
        self.key = key
        self.url = url
        self.description = description
        self.species = species
        self.home_world = home_world
        self.gender = gender
        self.skin_color = skin_color

    def __str__(self):
        return f"{self.name} is from {self.home_world}. Description: {self.description}. More details can be found here: {self.url}"

    @property
    def home_world(self):
        return self._home_world

    @home_world.setter
    def home_world(self, home_world):
        if home_world == "":
            self._home_world = "Unknown"
        else:
            self._home_world = home_world


    @property
    def species(self):
        return self._species

    @species.setter
    def species(self, species):
        if species == "":
            self._species = "Unknown"
        else:
            self._species = species

    @staticmethod
    def get_character(characters, name):
        for character in characters:
            if character.name == name:
                return character
        return False

    @staticmethod
    def get_home_world(characters, world):
        return [
            character.name for character in characters if character.home_world == world
        ]

    @staticmethod
    def is_valid_world(characters, world):
        all_worlds = [character.home_world for character in characters]
        if world in all_worlds:
            return True
        return False

    @staticmethod
    def get_species(characters, species):
        return [
            character.name for character in characters if character.species == species
        ]

    @staticmethod
    def is_valid_species(characters, species):
        all_species = [character.species for character in characters]
        if species in all_species:
            return True
        return False


if __name__ == "__main__":
    main()