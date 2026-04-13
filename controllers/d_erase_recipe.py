from data.e_save_recipes import save_recipes

def erase_recipe(all_recipes):

    print("\nRezept löschen")

    recipe_name = input("Name des Rezepts: ").strip()

    if recipe_name in all_recipes:
        del all_recipes[recipe_name]
        save_recipes(all_recipes)
        print(f"Rezept '{recipe_name}' gelöscht.")
    else:
        print("Rezept nicht gefunden.")