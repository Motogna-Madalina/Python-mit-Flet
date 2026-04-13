

def get_valid_name(all_recipes):

    while True:
        name = input("Name des Rezepts: ")

        if name.strip() == "":
            print("Der Name darf nicht leer sein.")
        elif len(name) > 200:
            print("Max 200 Zeichen.")
        elif not name.replace(" ", "").isalpha():
            print("Nur Buchstaben erlaubt.")
        elif name in all_recipes:
            print("Rezept existiert bereits.")
        else:
            return name


def get_valid_ingredients():

    while True:
        ingredients = input("Zutaten (durch Komma getrennt): ").split(",")

        valid = True

        for each in ingredients:
            clean = each.strip()

            if clean == "":
                print("Leere Zutat.")
                valid = False
                break
            elif len(clean) > 100:
                print("Zu lang.")
                valid = False
                break
            elif not clean.replace(" ", "").isalnum():
                print("Ungültige Zeichen.")
                valid = False
                break

        if valid:
            return [i.strip() for i in ingredients]


def get_valid_instructions():

    while True:
        instructions = input("Anleitung: ")

        if instructions.strip() == "":
            print("Darf nicht leer sein.")
        else:
            return instructions


def add_recipe(all_recipes):

    print("\nNeues Rezept hinzufügen")

    recipe_name = get_valid_name(all_recipes)
    ingredients = get_valid_ingredients()
    instructions = get_valid_instructions()

    all_recipes[recipe_name] = {
        "zutaten": ingredients,
        "anleitung": instructions
    }


    print(f"Rezept '{recipe_name}' wurde hinzugefügt!")