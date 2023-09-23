import pytest
from star_wars_lib import Character
import csv
from sw_char import build_characters


def test_is_valid_world():
    characters = [
        Character(
            name="Luke Skywalker",
            key="luke-skywalker",
            url="https://example.com/luke",
            description="A Jedi Knight",
            species="Human",
            home_world="Tatooine",
            gender="Male",
            skin_color="Fair",
        ),
        Character(
            name="Leia Organa",
            key="leia-organa",
            url="https://example.com/leia",
            description="A Rebel Leader",
            species="Human",
            home_world="Alderaan",
            gender="Female",
            skin_color="Light",
        ),
    ]
    assert Character.is_valid_world(characters, "Tatooine") == True
    assert Character.is_valid_world(characters, "Alderaan") == True
    assert Character.is_valid_world(characters, "Hoth") == False

def test_get_species():
    characters = [
        Character(
            name="Luke Skywalker",
            key="luke-skywalker",
            url="https://example.com/luke",
            description="A Jedi Knight",
            species="Human",
            home_world="Tatooine",
            gender="Male",
            skin_color="Fair",
        ),
    ]

    assert Character.get_species(characters, "Human") == ["Luke Skywalker"]
    assert Character.get_species(characters, "Rodian") == []
    

def test_get_home_world():
    characters = [
        Character(
            name="Luke Skywalker",
            key="luke-skywalker",
            url="https://example.com/luke",
            description="A Jedi Knight",
            species="Human",
            home_world="Tatooine",
            gender="Male",
            skin_color="Fair",
        ),
        Character(
            name="Leia Organa",
            key="leia-organa",
            url="https://example.com/leia",
            description="A Rebel Leader",
            species="Human",
            home_world="Alderaan",
            gender="Female",
            skin_color="Light",
        ),
    ]
    assert Character.get_home_world(characters, "Tatooine") == ["Luke Skywalker"]
    assert Character.get_home_world(characters, "Alderaan") == ["Leia Organa"]
    assert Character.get_home_world(characters, "Hoth") == []

def test_get_character():
    characters = [
        Character(
            name="Luke Skywalker",
            key="luke-skywalker",
            url="https://example.com/luke",
            description="A Jedi Knight",
            species="Human",
            home_world="Tatooine",
            gender="Male",
            skin_color="Fair",
        ),
        Character(
            name="Leia Organa",
            key="leia-organa",
            url="https://example.com/leia",
            description="A Rebel Leader",
            species="Human",
            home_world="Alderaan",
            gender="Female",
            skin_color="Light",
        ),
    ]
    assert Character.get_character(characters, "Luke Skywalker") == characters[0]
    assert Character.get_character(characters, "Darth Vader") == False


def test_character_species():
    character = Character(
        name="Luke Skywalker",
        key="luke-skywalker",
        url="https://example.com/luke",
        description="A Jedi Knight",
        species="Human",
        home_world="Tatooine",
        gender="Male",
        skin_color="Fair",
    )
    assert character.species == "Human"

    character.species = ""
    assert character.species == "Unknown"

def test_character_home_world():
    character = Character(
        name="Luke Skywalker",
        key="luke-skywalker",
        url="https://example.com/luke",
        description="A Jedi Knight",
        species="Human",
        home_world="Tatooine",
        gender="Male",
        skin_color="Fair",
    )
    assert character.home_world == "Tatooine"

    character.home_world = ""
    assert character.home_world == "Unknown"

