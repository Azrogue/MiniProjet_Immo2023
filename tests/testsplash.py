import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image

class MenuWindow(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("Menu")
        self.master.geometry("800x600")

        # Chargement des images
        self.recherche_img = ImageTk.PhotoImage(Image.open("recherche.jpg"))
        self.enregistrement_img = ImageTk.PhotoImage(Image.open("enregistrement.jpg"))

        # Création des deux rectangles
        self.recherche_rect = tk.Canvas(self.master, width=400, height=600, bg="white")
        self.recherche_rect.pack(side=tk.LEFT)
        self.enregistrement_rect = tk.Canvas(self.master, width=400, height=600, bg="white")
        self.enregistrement_rect.pack(side=tk.RIGHT)

        # Ajout des images aux rectangles
        self.recherche_rect.create_image(0, 0, anchor=tk.NW, image=self.recherche_img)
        self.enregistrement_rect.create_image(0, 0, anchor=tk.NW, image=self.enregistrement_img)

        # Ajout des titres aux rectangles
        recherche_title = tk.Label(self.recherche_rect, text="Recherche de biens", font=("Arial", 20), bg="white")
        recherche_title.place(relx=0.5, rely=0.3, anchor=tk.CENTER)
        enregistrement_title = tk.Label(self.enregistrement_rect, text="Enregistrement de biens", font=("Arial", 20), bg="white")
        enregistrement_title.place(relx=0.5, rely=0.3, anchor=tk.CENTER)

        # Ajout des descriptions aux rectangles
        recherche_description = tk.Label(self.recherche_rect, text="Trouvez le bien immobilier de vos rêves", font=("Arial", 12), bg="white")
        recherche_description.place(relx=0.5, rely=0.4, anchor=tk.CENTER)
        enregistrement_description = tk.Label(self.enregistrement_rect, text="Enregistrez un nouveau bien immobilier dans la base de données", font=("Arial", 12), bg="white")
        enregistrement_description.place(relx=0.5, rely=0.4, anchor=tk.CENTER)

        # Ajout des boutons "Accéder" aux rectangles
        recherche_button = tk.Button(self.recherche_rect, text="Accéder", font=("Arial", 12), bg="white", fg="black", command=self.on_recherche_click)
        recherche_button.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        enregistrement_button = tk.Button(self.enregistrement_rect, text="Accéder", font=("Arial", 12), bg="white", fg="black", command=self.on_enregistrement_click)
        enregistrement_button.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    def on_recherche_click(self):
        messagebox.showinfo("Recherche de biens", "Vous avez choisi de rechercher des biens")

    def on_enregistrement_click(self):
        messagebox.showinfo("Enregistrement de biens", "Vous avez choisi d'enregistrer des biens")

# Créer une fenêtre principale
root = tk.Tk()
root.withdraw()

# Titre de la fenêtre
root.title("Gestion Immobilière")
# Création de la fenêtre de choix
choice_window = tk.Toplevel(root)
choice_window.title("Choix")
choice_window.geometry("800x400")

# Chargement des images pour les rectangles
search_img = Image.open("search.jpg")
search_img = search_img.resize((400, 400))
search_img = ImageTk.PhotoImage(search_img)

register_img = Image.open("register.jpg")
register_img = register_img.resize((400, 400))
register_img = ImageTk.PhotoImage(register_img)

# Création des rectangles pour les images
search_rect = tk.Label(choice_window, image=search_img)
search_rect.place(x=0, y=0)

register_rect = tk.Label(choice_window, image=register_img)
register_rect.place(x=400, y=0)

# Titre et description pour la recherche de biens
search_title = tk.Label(choice_window, text="Recherche de biens", font=("Arial", 24), bg="#F2F2F2")
search_title.place(x=50, y=50)

search_desc = tk.Label(choice_window, text="Effectuer une recherche dans la base de données des biens immobiliers", font=("Arial", 14), bg="#F2F2F2")
search_desc.place(x=50, y=120)

# Bouton pour la recherche de biens
search_button = tk.Button(choice_window, text="Accéder", font=("Arial", 14), bg="#FFFFFF", fg="#000000")
search_button.place(x=50, y=200)

# Titre et description pour l'enregistrement de biens
register_title = tk.Label(choice_window, text="Enregistrement de biens", font=("Arial", 24), bg="#F2F2F2")
register_title.place(x=450, y=50)

register_desc = tk.Label(choice_window, text="Enregistrer un nouveau bien immobilier dans la base de données", font=("Arial", 14), bg="#F2F2F2")
register_desc.place(x=450, y=120)

# Bouton pour l'enregistrement de biens
register_button = tk.Button(choice_window, text="Accéder", font=("Arial", 14), bg="#FFFFFF", fg="#000000")
register_button.place(x=450, y=200)

# Boucle principale pour afficher la fenêtre de choix
choice_window.mainloop()

