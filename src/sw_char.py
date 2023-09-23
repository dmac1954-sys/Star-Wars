import csv
import sys
from star_wars_lib import Character 


def main():
    characters = build_characters()
    while True:
        choice = int(
            input(
                "Please enter \n1 to find all characters of a specific species\n2 to find all characters of a specific home world\n3 to find a specific character\n4 to quit the program.\nEnter choice: "
            )
        )
        if choice == 1:
            species = input("Please enter a species: ")
            if Character.is_valid_species(characters, species):
                # validation to come
                result = Character.get_species(characters, species)
                result = "\n".join(result)
                print(result)

            else:
                print("This species could not be found!")
                continue

        elif choice == 2:
            world = input("Please enter a home world: ")
            if Character.is_valid_world(characters, world):
                result = Character.get_home_world(characters, world)
                result = "\n".join(result)
                print(result)

            else:
                print("This world could not be found!")
                continue

        elif choice == 3:
            name = input("Please enter a characters name: ")
            # validation to come

            result = Character.get_character(characters, name)
            if not result:
                print("This character could not be found!")
                continue
            else:
                print(f"Name: {result.name}")
                print(f"Species: {result.species}")
                print(f"Gender: {result.gender}")
                print(f"Skin color: {result.skin_color}")
                print(f"Home world: {result.home_world}")
                print(f"Key: {result.key}")
                print(f"Description: {result.description}")
                print(f"URL: {result.url}")

        else:
            sys.exit("Program quitting.....")


def build_characters():
    characters = []
    with open("./src/output.csv", "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            name = row["name"]
            key = row["key"]
            url = row["url"]
            description = row["description"]
            species = row["species"]
            home_world = row["home_world"]
            gender = row["gender"]
            skin_color = row["skin_color"]
            new_char = Character(
                name, key, url, description, species, home_world, gender, skin_color
            )
            characters.append(new_char)

    return characters


if __name__ == "__main__":
    main()
