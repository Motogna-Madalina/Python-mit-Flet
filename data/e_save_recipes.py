import json
def save_recipes(all_recipes):
    try:
        with open('data/recipes.json', 'w', encoding='utf-8') as file:
            json.dump(all_recipes, file, ensure_ascii=False, indent=4)
    except Exception as e:
        print("Fehler beim Speichern:", e)