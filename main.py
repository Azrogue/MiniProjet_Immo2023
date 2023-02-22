import tkinter as tk
from tkinter import messagebox
# from PIL import ImageTk, Image
import sqlite3
import time
import os


# ===================================
#              FONCTIONS
# ===================================
# Chemin de la base de données
db_file = "bien_immo.db"

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





# Créer deux frames pour les deux options
left_frame = tk.Frame(root, width=width/2, height=height)
right_frame = tk.Frame(root, width=width/2, height=height)
left_frame.pack(side=tk.LEFT)
right_frame.pack(side=tk.RIGHT)

# Ajouter les images de fond
#left_image = tk.PhotoImage(file="Assets/img/left_image.png").subsample(2)
#right_image = tk.PhotoImage(file="Assets/img/right_image.png").subsample(2)
#left_label = tk.Label(left_frame, image=left_image)
#right_label = tk.Label(right_frame, image=right_image)
#left_label.pack(fill=tk.BOTH, expand=True)
#right_label.pack(fill=tk.BOTH, expand=True)

# Ajouter les titres et descriptions
left_title = tk.Label(left_frame, text="Recherche de biens", font=("Helvetica", 20))
right_title = tk.Label(right_frame, text="Enregistrement de biens", font=("Helvetica", 20))
left_title.pack(pady=(20, 10), anchor="center")
right_title.pack(pady=(20, 10), anchor="center")

left_description = tk.Label(left_frame, text="Rechercher des biens existants", font=("Helvetica", 12))
right_description = tk.Label(right_frame, text="Enregistrer un nouveau bien", font=("Helvetica", 12))
left_description.pack(pady=(10, 20), anchor="center")
right_description.pack(pady=(10, 20), anchor="center")

# Ajouter les boutons d'accès
left_button = tk.Button(left_frame, text="Accéder", bg="white", fg="black", font=("Helvetica", 14))
right_button = tk.Button(right_frame, text="Accéder", bg="white", fg="black", font=("Helvetica", 14))
left_button.pack(pady=(10, 20), anchor="center")
right_button.pack(pady=(10, 20), anchor="center")


# Start the event loop
root.deiconify()
splash_screen.destroy()
root.mainloop()