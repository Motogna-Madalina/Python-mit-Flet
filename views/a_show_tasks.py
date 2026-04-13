from models.data_all_tasks import all_tasks 
#from controllers.b_user_ingredients import user_ingredients, find_recipes

#we are making here a loop in another loop
#the first loop goes through all the recipes, and the second loop goes through the ingredients and instructions of each recipe.
#recipe is the name of the recipe, and details is a dictionary that contains the ingredients and instructions for that recipe.


def show_all_tasks(all_tasks):
    for task, details in all_tasks.items():
        print(f"\nTask: {task}")
        print("-------------------------")
        print(f"\nName: {details['name']}")
        print(f"Beschreibung: {details['beschreibung']}")
        print(f"Status: {details['status']}\n")

        