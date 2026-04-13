
from data.load_data import load_json_file
<<<<<<< HEAD
from controllers.c_add_recipe import add_recipe
from controllers.b_find_recipe import user_ingredients, find_recipes
from controllers.d_erase_recipe import erase_recipe
from data.e_save_recipes import save_recipes
from controllers.g_edit_recipe import edit_recipe
from views import a_show_recipes
from views.a_show_recipes import show_all_recipes
=======
from controllers.b_add_task import add_task
from data.q_save_data import save_data
from views.a_show_tasks import show_all_tasks
from controllers.c_edit_task import edit_status
from controllers.d_find_task import *

all_tasks = load_json_file()
>>>>>>> 3b630b096013ef7150cd1404b76f6e5d173fda5d


#our program is a simple task management system that allows the user to add tasks,
#view all tasks, edit the status of a task, and search for tasks. The tasks 
#are stored in a JSON file and loaded into a dictionary when the program starts.

#The user can interact with the program through a simple text-based menu. 

#The program will continue to run until the user chooses to quit, 
#at which point the data will be saved back to the JSON file.

#Thank you for your attention and I hope you enjoy using TaskHub to manage
#your tasks and improve your organization!

while True:
        print("\nWillkommen bei TaskHub!")
        print("\nDieses Programm hilft Ihnen dabei, Ihre Organisation zu verbessern.")
        print("A - Alle Aufgaben anzeigen")
        print("B - Neue Aufgabe hinzufügen")
        print("C - Aufgabe als erledigt markieren / wieder öffnen")
        print("D - Aufgaben suchen")
        print("Q - Daten speichern und Programm beenden")
        print("\nBitte wählen Sie eine Option aus: ")

        choice = input("Ihre Auswahl: ").upper()

        if choice == "A":
            show_all_tasks(all_tasks)

        elif choice == "B":
            add_task(all_tasks)
    
        elif choice == "C":
            edit_status(all_tasks)

        elif choice == "D":
            find_tasks(all_tasks)

<<<<<<< HEAD
        elif choice == "F":
            a_show_recipes(all_recipes)
            print("Rezepte geladen!")

        elif choice == "G":
            edit_recipe(all_recipes)

        elif choice == "H":
            save_recipes(all_recipes)
            print("Programm beendet. Auf Wiedersehen!")
=======
        elif choice == "Q":
            save_data(all_tasks)
            print("Daten gespeichert. Programm beendet!")
>>>>>>> 3b630b096013ef7150cd1404b76f6e5d173fda5d
            break

        else:
            print("Ungültige Auswahl!")


