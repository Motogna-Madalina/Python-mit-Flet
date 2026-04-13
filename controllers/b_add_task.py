from models.data_all_tasks import all_tasks


def get_valid_id():

    while True:
        id = input("ID: ")

        if id.strip() == "":
            print("Die ID darf nicht leer sein.")
        elif len(id) > 200:
            print("Max 200 Zeichen.")
        elif not id.isdigit():
            print("Nur nummerische Zeichen erlaubt.")
    
        else:
            return id


def get_valid_name():

    while True:
        name = input("Name der Aufgabe: ")

        if name.strip() == "":
            print("Der Name darf nicht leer sein.")
        elif len(name) > 200:
            print("Max 200 Zeichen.")
        elif not name.replace(" ", "").isalpha():
            print("Nur Buchstaben erlaubt.")
        elif name in all_tasks:
            print("Aufgabe existiert bereits.")
        else:
            return name
        
def get_valid_description():

    while True:
        description = input("Beschreibung: ")
        if description.strip() == "":
            print("Die Beschreibung darf nicht leer sein.")
        elif len(description) > 500:
            print("Max 500 Zeichen.")
        else:
            return description


def add_task(all_tasks):

    print("\nNeue Aufgabe hinzufügen")

    task_id = get_valid_id()
    task_name = get_valid_name()
    description = get_valid_description()

    all_tasks[task_id] = {
        "name": task_name,
        "beschreibung": description,
        "status": "offen"
    }


    print(f"Aufgabe '{task_name}' wurde hinzugefügt!")