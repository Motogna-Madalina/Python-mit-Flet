from views.a_show_tasks import show_all_tasks


def edit_status(all_tasks):
        
    while True:     
        task_id = input("Geben Sie die ID der Aufgabe ein, deren Status Sie ändern möchten: ")
        if task_id in all_tasks:
                current_status = all_tasks[task_id]["status"]
                new_status = "erledigt" if current_status == "offen" else "offen"
                all_tasks[task_id]["status"] = new_status
                print(f"Der Status der Aufgabe '{all_tasks[task_id]['name']}' wurde auf '{new_status}' geändert.")
                break
        else:
                print("Ungültige ID. Bitte versuchen Sie es erneut.")