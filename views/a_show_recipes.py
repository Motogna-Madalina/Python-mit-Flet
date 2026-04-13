

#we are making here a loop in another loop
#the first loop goes through all the recipes, and the second loop goes through the ingredients and instructions of each recipe.
#recipe is the name of the recipe, and details is a dictionary that contains the ingredients and instructions for that recipe.


def show_all_recipes(all_recipes):
    for recipe, details in all_recipes.items():
        #recipe
        print("\nRezept:", recipe)

        #ingredients
        print("Zutaten:")
        for ingredient in details["zutaten"]:
            print("-", ingredient)
            
        #instructions
        print("Anleitung:")
        print(details["anleitung"])


