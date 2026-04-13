import flet as ft
from data.load_data import load_json_file
from data.e_save_recipes import save_recipes

all_recipes = load_json_file()

def main(page: ft.Page):
    page.title = "Recipe Manager"
    page.scroll = "auto"
    page.bgcolor = "#F8F7F4"

    content = ft.Column()
                            #ft.Column means a vertical layout container that stacks its child controls vertically.
                            #It is used to organize and arrange the UI elements in a vertical manner on the page.

    def show_recipes(e=None):
        import os
        content.controls.clear()
        cards = []
        for name, r in all_recipes.items():
            image_path = "static/images/" + r.get("image", "default.jpg")
            has_img = r.get("image") and r.get("image") != "default.jpg" and os.path.exists(image_path)
            img = ft.Image(src=image_path, width=280, height=160, fit="cover", border_radius=ft.border_radius.only(top_left=14, top_right=14)) if has_img                   else ft.Container(width=280, height=160, bgcolor="#D8F3DC",
                                    border_radius=ft.border_radius.only(top_left=14, top_right=14),
                                    content=ft.Text("🍽", size=48), alignment=ft.alignment.Alignment(0,0))
            card = ft.Container(
                content=ft.Column([
                    img,
                    ft.Container(
                        content=ft.Column([
                            ft.Text(name, size=16, weight="bold", color="#1A1A18"),
                            ft.Text(", ".join(r["zutaten"]), size=12, color="#2D6A4F", max_lines=2, overflow=ft.TextOverflow.ELLIPSIS),
                            ft.Text(r["anleitung"], size=12, color="#5A5A55", max_lines=2, overflow=ft.TextOverflow.ELLIPSIS),
                            ft.Row([
                                ft.ElevatedButton("✏️", on_click=lambda e, n=name: edit_recipe_ui(n), bgcolor="#EFF6FF", color="#2563EB", elevation=0),
                                ft.ElevatedButton("🗑", on_click=lambda e, n=name: quick_delete(n),   bgcolor="#FEF2F2", color="#DC2626", elevation=0),
                            ], alignment=ft.MainAxisAlignment.END),
                        ], spacing=6),
                        padding=14,
                    ),
                ], spacing=0),
                border_radius=14, bgcolor="white",
                border=ft.border.all(1, "#ECEAE6"),
                width=280,
            )
            cards.append(card)
        if not cards:
            content.controls.append(ft.Text("Keine Rezepte.", color="#9A9A95"))
        else:
            content.controls.append(ft.Row(controls=cards, wrap=True, spacing=16, run_spacing=16))
        page.update()

    def quick_delete(name):
        if name in all_recipes:
            del all_recipes[name]
            save_recipes(all_recipes)
        show_recipes()

    def edit_recipe_ui(name):
        r = all_recipes[name]
        zutaten   = ft.TextField(label="Zutaten", value=", ".join(r["zutaten"]), border_radius=10, bgcolor="white", border_color="#ECEAE6", focused_border_color="#2D6A4F")
        anleitung = ft.TextField(label="Anleitung", value=r["anleitung"], multiline=True, min_lines=2, border_radius=10, bgcolor="white", border_color="#ECEAE6", focused_border_color="#2D6A4F")
        def save(e):
            all_recipes[name]["zutaten"]  = [x.strip() for x in zutaten.value.split(",")]
            all_recipes[name]["anleitung"] = anleitung.value.strip()
            save_recipes(all_recipes)
            show_recipes()
        content.controls.clear()
        content.controls.append(ft.Column([
            ft.Text(f"Bearbeiten: {name}", size=20, weight="bold", color="#1A1A18"),
            zutaten, anleitung,
            ft.Row([
                ft.TextButton("Zurück", on_click=show_recipes),
                ft.ElevatedButton("Speichern", on_click=save, bgcolor="#2D6A4F", color="white", elevation=0),
            ], alignment=ft.MainAxisAlignment.END),
        ], spacing=10))
        page.update()

    def add_recipe_ui(e):
        content.controls.clear()
        name      = ft.TextField(label="Name", border_radius=10, bgcolor="white", border_color="#ECEAE6", focused_border_color="#2D6A4F")
        zutaten   = ft.TextField(label="Zutaten (mit Komma)", border_radius=10, bgcolor="white", border_color="#ECEAE6", focused_border_color="#2D6A4F")
        anleitung = ft.TextField(label="Anleitung", multiline=True, min_lines=2, border_radius=10, bgcolor="white", border_color="#ECEAE6", focused_border_color="#2D6A4F")
        def save(e):
            all_recipes[name.value.strip()] = {
                "zutaten": [x.strip() for x in zutaten.value.split(",")],
                "anleitung": anleitung.value.strip()
            }
            save_recipes(all_recipes)
            show_recipes()
        content.controls.append(ft.Column([
            ft.Text("Neues Rezept", size=20, weight="bold", color="#1A1A18"),
            name, zutaten, anleitung,
            ft.Row([
                ft.TextButton("Zurück", on_click=show_recipes),
                ft.ElevatedButton("Speichern", on_click=save, bgcolor="#2D6A4F", color="white", elevation=0),
            ], alignment=ft.MainAxisAlignment.END),
        ], spacing=10))
        page.update()

    def search_recipe(e):
        content.controls.clear()
        search = ft.TextField(
            label="Zutaten suchen",
            hint_text="z.B. Mehl, Wasser, Salz, Hefe ...",
            
            border_radius=10, bgcolor="white",
            border_color="#ECEAE6", focused_border_color="#2D6A4F",
        )
        results = ft.Column(spacing=8)
        def do_search(e):
            user_ings = [x.strip().lower() for x in search.value.split(",") if x.strip()][:10]
            results.controls.clear()
            if not user_ings:
                results.controls.append(ft.Text("Bitte Zutaten eingeben.", color="#9A9A95"))
                page.update()
                return
            found = False
            for name, r in all_recipes.items():
                recipe_ings = " ".join(r["zutaten"]).lower()
                if any(ing in recipe_ings for ing in user_ings):
                    matched = [ing for ing in user_ings if ing in recipe_ings]
                    results.controls.append(
                        ft.Container(
                            content=ft.Column([
                                ft.Text("✅ " + name, color="#2D6A4F", weight="bold", size=15),
                                ft.Text("Gefunden: " + ", ".join(matched), size=12, color="#5A5A55"),
                            ], spacing=2),
                            bgcolor="white", border_radius=10, padding=12,
                            border=ft.border.all(1, "#ECEAE6"),
                        )
                    )
                    found = True
            if not found:
                results.controls.append(ft.Text("Keine Treffer.", color="#9A9A95"))
            page.update()
        content.controls.append(ft.Column([
            ft.Text("Suche nach Zutaten", size=20, weight="bold", color="#1A1A18"),
            search,
            ft.Row([
                ft.TextButton("Zuruck", on_click=show_recipes),
                ft.ElevatedButton("Suchen", on_click=do_search, bgcolor="#2D6A4F", color="white", elevation=0),
            ], alignment=ft.MainAxisAlignment.END),
            results,
        ], spacing=10))
        page.update()

    def delete_recipe(e):
        content.controls.clear()
        name = ft.TextField(label="Rezeptname", border_radius=10, bgcolor="white", border_color="#ECEAE6", focused_border_color="#2D6A4F")
        def delete(e):
            if name.value in all_recipes:
                del all_recipes[name.value]
                save_recipes(all_recipes)
            show_recipes()
        content.controls.append(ft.Column([
            ft.Text("Rezept löschen", size=20, weight="bold", color="#1A1A18"),
            name,
            ft.Row([
                ft.TextButton("Zurück", on_click=show_recipes),
                ft.ElevatedButton("Löschen", on_click=delete, bgcolor="#DC2626", color="white", elevation=0),
            ], alignment=ft.MainAxisAlignment.END),
        ], spacing=10))
        page.update()

    def save_all(e):
        save_recipes(all_recipes)

    menu = ft.Container(
        bgcolor="white",
        border=ft.border.only(bottom=ft.BorderSide(1, "#ECEAE6")),
        padding=ft.padding.symmetric(horizontal=20, vertical=12),
        content=ft.Row([
            ft.Text("🍲 Recipe Manager", size=20, weight="bold", color="#1A1A18"),
            ft.Row([
                ft.ElevatedButton("📋 Alle Rezepte", on_click=show_recipes, bgcolor="#D8F3DC", color="#2D6A4F", elevation=0),
                ft.ElevatedButton("🔍 Suche",        on_click=search_recipe, bgcolor="#D8F3DC", color="#2D6A4F", elevation=0),
                ft.ElevatedButton("➕ Hinzufügen",   on_click=add_recipe_ui, bgcolor="#2D6A4F", color="white",  elevation=0),
                ft.ElevatedButton("🗑 Löschen",      on_click=delete_recipe, bgcolor="#FEF2F2", color="#DC2626", elevation=0),
                ft.ElevatedButton("💾 Speichern",    on_click=save_all,      bgcolor="#F0F9FF", color="#2563EB", elevation=0),
            ], spacing=6),
        ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
    )

    page.add(menu, ft.Container(content=content, padding=20))
    show_recipes()

ft.app(target=main)