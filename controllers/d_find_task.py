
from models.data_all_tasks import all_tasks

def user_get_words():

    user_input = input("Gib die Stichwörter ein, nach denen du suchen möchtest: ").split(",")
    cleaned_words = []    

    for item in user_input:
        keyword = item.strip().lower()
        cleaned_words.append(keyword)   
    return cleaned_words

def find_tasks(all_tasks):
    user_words = user_get_words()

    print("\nPassende Aufgaben:")
    found = False
    while True:
        for task in all_tasks:
            task_name = all_tasks[task]["name"].lower()
            if any(word in task_name for word in user_words):
                print("-", all_tasks[task]["name"] + " (ID: " + task + ") - Status: " + all_tasks[task]["status"] + "\nBeschreibung: " + all_tasks[task]["beschreibung"])
                found = True
                
        if found:
            break
        if not found:
        
            print("Keine passenden Aufgaben gefunden.")