

def edit_recipe(all_recipes):
        
        while True:
            print("\n--- Rezept bearbeiten ---")
            print("Rezeptbearbeitung- druck 1")
            print("Wider in menü zurück- druck 2")
            choice = input("Ihre Auswahl: ")    

            if choice == "1":   
                

                recipe_name = input("Geben Sie den Namen des Rezepts ein, das Sie bearbeiten möchten: ")

                if recipe_name in all_recipes:
                    print(f"Wählen Sie die Option, die Sie bearbeiten möchten: ")
                    print("1 - Zutaten")
                    print("2 - Anleitung") 
                    print("3 - Beides")
                    print("4 - Abbrechen")
                    choice = input("Ihre Auswahl: ")

                    if choice == "1":   
                        print(f"Aktuelle Zutaten für {recipe_name}: {all_recipes[recipe_name]['zutaten']}")
                        new_ingredients = input("Geben Sie die neuen Zutaten ein (durch Kommas getrennt): ")
                        all_recipes[recipe_name]['zutaten'] = [ingredient.strip() for ingredient in new_ingredients.split(',')]
                        print(f"Rezept '{recipe_name}' wurde aktualisiert.")   


                    elif choice == "2":     
                        print(f"Neue Anleitung für {recipe_name}: {all_recipes[recipe_name]['anleitung']}")
                        new_instructions = input("Geben Sie die neuen Anweisungen ein: ")                                       
                        all_recipes[recipe_name]['anleitung'] = new_instructions.strip()
                        print(f"Rezept '{recipe_name}' wurde aktualisiert.")  

                    elif choice == "3":
                        print(f"Aktuelle Zutaten für {recipe_name}: {all_recipes[recipe_name]['zutaten']}")
                        new_ingredients = input("Geben Sie die neuen Zutaten ein (durch Kommas getrennt): ")
                        all_recipes[recipe_name]['zutaten'] = [ingredient.strip() for ingredient in new_ingredients.split(',')]

                        print(f"Neue Anleitung für {recipe_name}: {all_recipes[recipe_name]['anleitung']}")
                        new_instructions = input("Geben Sie die neuen Anweisungen ein: ")
                        all_recipes[recipe_name]['anleitung'] = new_instructions.strip()
                        print(f"Rezept '{recipe_name}' wurde aktualisiert.")
                    
                    elif choice == "4":
                        print("Bearbeitung abgebrochen.")
                        print("Rückkehr zum Hauptmenü.")
                        break

                    else:
                        print("Ungültige Auswahl.")

                else:
                    print(f"Rezept '{recipe_name}' nicht gefunden.")

            elif choice == "2":
                print("Rückkehr zum Hauptmenü.")
                break

            else:    
                 print("Ungültige Auswahl.")