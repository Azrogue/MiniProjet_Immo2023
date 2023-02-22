import tkinter as tk
from tkinter import messagebox
import sqlite3
import time
import os


# ===================================
#              FONCTIONS
# ===================================
# Chemin de la base de données
db_file = "bien_immo.sqlite"

# ===================================
#                SQL
# ===================================


def create_database(db_file):
    """Crée une base de données SQLite avec une table 'biens_immobiliers'"""

    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS biens_immobiliers (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        type_immobilier TEXT,
        adresse TEXT,
        superficie_couvert REAL,
        superficie_jardin REAL,
        nombre_pieces INTEGER,
        classe_energetique TEXT,
        annee_construction INTEGER,
        nature_gestion TEXT,
        date_mise_marche TEXT,
        prix REAL
    )
    """)

    conn.commit()
    conn.close()


def inserer_bien_immobilier(db_file, bien):
    """Insert un bien immobilier dans la table 'biens_immobiliers' de la base de données SQLite"""

    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO biens_immobiliers (
        type_immobilier,
        adresse,
        superficie_couvert,
        superficie_jardin,
        nombre_pieces,
        classe_energetique,
        annee_construction,
        nature_gestion,
        date_mise_marche,
        prix
    )
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        bien['type_immobilier'],
        bien['adresse'],
        bien['superficie_couvert'],
        bien['superficie_jardin'],
        bien['nombre_pieces'],
        bien['classe_energetique'],
        bien['annee_construction'],
        bien['nature_gestion'],
        bien['date_mise_marche'],
        bien['prix']
    ))

    conn.commit()
    conn.close()

def recuperation_infos_bien(db_file):
    # Connexion à la base de données
    conn = sqlite3.connect('biens_immo.db')

    # Récupération des biens immobiliers
    biens_immo = []
    cursor = conn.execute('SELECT * FROM biens')
    for row in cursor:
        biens_immo.append(row)

    # Fermeture de la connexion
    conn.close()

def centerWindow(width, height, root):  # Return 4 values needed to center Window
    screen_width = root.winfo_screenwidth()  # Width of the screen
    screen_height = root.winfo_screenheight() # Height of the screen     
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    return int(x), int(y)


# ===================================
#              EXECUTION
# ===================================
# Créer une fenêtre principale
root = tk.Tk()
root.withdraw()

# Titre de la fenêtre
root.title("Gestion Immobilière")

# SPLASH SCREEN CODE
splash_screen = tk.Toplevel(background="white")
splash_screen.overrideredirect(True)
splash_screen.title("Splash Screen")
x, y = centerWindow(600, 400, root)
splash_screen.geometry(f"600x400+{x}+{y}")
 
image = tk.PhotoImage(file="Assets/img/splash.png") 
label = tk.Label(splash_screen, image = image)
label.pack()
splash_screen.update()


# Obtenir la taille de l'écran
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()


# Définir la taille de la fenêtre en fonction de la taille de l'écran
ratio = 0.8  # On définit un ratio pour la taille de la fenêtre
width = int(screen_width * ratio)
height = int(screen_height * ratio)
root.geometry(f"{width}x{height}")

# MAIN WINDOW CODE + Other Processing
time.sleep(4)

# Vérification de l'existence de la base de données
if not os.path.isfile(db_file):
    root = tk.Tk()
    root.withdraw()

    if messagebox.askyesno("Créer la base de données", "La base de données n'existe pas encore, voulez-vous la créer ?"):
        create_database(db_file)
    else:
        messagebox.showinfo("Fermeture de Pymmobilier", "Le programme va se fermer")
        exit()

label_type = tk.Label(root, text="Type de bien")
label_type.grid(row=2, column=0)

# Création des boutons radio
type_var = tk.StringVar()
type_var.set("Maison")
radio1 = tk.Radiobutton(root, text="Maison", variable=type_var, value="Maison")
radio2 = tk.Radiobutton(root, text="Appartement", variable=type_var, value="Appartement")
radio1.grid(row=2, column=1)
radio2.grid(row=2, column=2)
type_bien_label = tk.Label(root, text="Type de bien")
adresse_label = tk.Label(root, text="Adresse")
superficie_label = tk.Label(root, text="Superficie (en m²)")
nombre_pieces_label = tk.Label(root, text="Nombre de pièces")
prix_label = tk.Label(root, text="Prix (en €)")

# Placement des étiquettes sur la fenêtre
type_bien_label.grid(row=0, column=0)

adresse_label.grid(row=1, column=0)
superficie_label.grid(row=2, column=0)
nombre_pieces_label.grid(row=3, column=0)
prix_label.grid(row=4, column=0)

#Création des entrées pour chaque champ de formulaire
type_bien_entry = tk.Entry(root)
adresse_entry = tk.Entry(root)
superficie_entry = tk.Entry(root)
nombre_pieces_entry = tk.Entry(root)
prix_entry = tk.Entry(root)

#Placement des entrées sur la fenêtre
type_bien_entry.grid(row=0, column=1)
adresse_entry.grid(row=1, column=1)
superficie_entry.grid(row=2, column=1)
nombre_pieces_entry.grid(row=3, column=1)
prix_entry.grid(row=4, column=1)

#Création du bouton d'enregistrement
enregistrer_button = tk.Button(root, text="Enregistrer")

#Placement du bouton sur la fenêtre
enregistrer_button.grid(row=5, column=1)

# Start the event loop
root.deiconify()
splash_screen.destroy()
root.mainloop()