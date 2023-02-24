import tkinter as tk
from tkinter import messagebox
import sqlite3
import time
from datetime import date
import os


# ===================================
#              FONCTIONS
# ===================================
# Chemin de la base de données
db_file = "bien_immo.sqlite"

def create_database(db_file):
    """Crée une base de données SQLite avec une table 'biens_immobiliers'"""

    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS biens_immobiliers (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        type_immobilier TEXT,
        adresse_sans_ville TEXT,
        ville_cp_adresse TEXT,
        nr_adresse TEXT,
        type_voie_adresse TEXT,
        nom_voie_adresse TEXT,
        cp_adresse INTEGER,
        nom_ville_adresse TEXT,
        superficie_couvert REAL,
        superficie_jardin REAL,
        nombre_pieces INTEGER,
        classe_energetique TEXT,
        annee_construction INTEGER,
        nature_gestion TEXT,
        date_mise_marche TEXT,
        prix REAL,
        timestamp DATE DEFAULT (datetime('now','localtime'))
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
        adresse_sans_ville,
        ville_cp_adresse,
        nr_adresse,
        type_voie_adresse,
        nom_voie_adresse,
        cp_adresse,
        nom_ville_adresse,
        superficie_couvert,
        superficie_jardin,
        nombre_pieces,
        classe_energetique,
        annee_construction,
        nature_gestion,
        prix
    )
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?,?,?,?,?,?,?)
    """, (
        bien['type_immobilier'],
        bien['adresse_sans_ville'],
        bien['ville_cp_adresse'],
        bien['nr_adresse'],
        bien['type_voie_adresse'],
        bien['nom_voie_adresse'],
        bien['cp_adresse'],
        bien['nom_ville_adresse'],
        bien['superficie_couvert'],
        bien['superficie_jardin'],
        bien['nombre_pieces'],
        bien['classe_energetique'],
        bien['annee_construction'],
        bien['nature_gestion'],
        bien['prix']
    ))


    conn.commit()
    conn.close()



def ouvrir_ajout_bien_immobilier():

    # Création de la fenêtre d'ajout de bien immobilier
    global ajout_bien_immobilier_window
    ajout_bien_immobilier_window = tk.Toplevel(root)
    ajout_bien_immobilier_window.title("Ajouter un bien immobilier")
    ajout_bien_immobilier_window.geometry("500x600")

    global type_immobilier_value
    type_immobilier_value = tk.StringVar(value="Appartement")

    # Création des boutons radio pour le type d'immobilier
    type_immobilier_label = tk.Label(ajout_bien_immobilier_window, text="Type d'immobilier :")
    type_immobilier_label.grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)

    type_immobilier_appartement_radio = tk.Radiobutton(
        ajout_bien_immobilier_window,
        text="Appartement",
        variable=type_immobilier_value,
        value="Appartement"
    )
    type_immobilier_appartement_radio.grid(row=0, column=1, padx=10, pady=10, sticky=tk.W)

    type_immobilier_maison_radio = tk.Radiobutton(
        ajout_bien_immobilier_window,
        text="Maison",
        variable=type_immobilier_value,
        value="Maison"
    )
    type_immobilier_maison_radio.grid(row=0, column=2, padx=10, pady=10)

    adresse_label = tk.Label(ajout_bien_immobilier_window, text="Adresse :")
    adresse_label.grid(row=1, column=0, padx=10, pady=10, sticky=tk.W)
    global adresse_nr_entry
    adresse_nr_entry = tk.Entry(ajout_bien_immobilier_window, width=5)
    adresse_nr_entry.grid(row=1, column=1, padx=10, pady=10, sticky=tk.W)
    
    global adresse_type_voie_var
    adresse_type_voie_var = tk.StringVar(ajout_bien_immobilier_window)
    addresse_type_voie_choices = ["Rue", "Allee", "Boulevard", "Chemin"]
    adresse_type_voie_var.set(addresse_type_voie_choices[0])

    adresse_type_voie_dropdown = tk.OptionMenu(ajout_bien_immobilier_window, adresse_type_voie_var, *addresse_type_voie_choices)
    adresse_type_voie_dropdown.grid(row=1, column=2, padx=10, pady=10, sticky=tk.W)
    
    global adresse_nomvoie_entry
    adresse_nomvoie_entry = tk.Entry(ajout_bien_immobilier_window, width=8)
    adresse_nomvoie_entry.grid(row=2, column=1, padx=10, pady=10, sticky=tk.W)

    global cp_adresse_entry
    cp_adresse_entry = tk.Entry(ajout_bien_immobilier_window, width=6)
    cp_adresse_entry.grid(row=2, column=2, padx=10, pady=10, sticky=tk.W)

    global nom_ville_adresse_entry
    nom_ville_adresse_entry = tk.Entry(ajout_bien_immobilier_window,width= 8)
    nom_ville_adresse_entry.grid(row=2, column=3, padx=10, pady=10, sticky=tk.W)

    superficie_couvert_label = tk.Label(ajout_bien_immobilier_window, text="Superficie couverte (m²) :")
    superficie_couvert_label.grid(row=3, column=0, padx=10, pady=10, sticky=tk.W)

    validate_func = ajout_bien_immobilier_window.register(validate_input)
    global superficie_couvert_entry
    superficie_couvert_entry = tk.Entry(ajout_bien_immobilier_window, validate="key", validatecommand=(validate_func, "%P"))
    superficie_couvert_entry.grid(row=3, column=1, padx=10, pady=10)

    superficie_jardin_label = tk.Label(ajout_bien_immobilier_window, text="Superficie jardin (m²) :")
    superficie_jardin_label.grid(row=4, column=0, padx=10, pady=10, sticky=tk.W)

    validate_func = ajout_bien_immobilier_window.register(validate_input)
    global superficie_jardin_entry
    superficie_jardin_entry = tk.Entry(ajout_bien_immobilier_window, validate="key", validatecommand=(validate_func, "%P"))
    superficie_jardin_entry.grid(row=4, column=1, padx=10, pady=10)

    nombre_pieces_label = tk.Label(ajout_bien_immobilier_window, text="Nombre de pièces :")
    nombre_pieces_label.grid(row=5, column=0, padx=10, pady=10, sticky=tk.W)

    validate_func = ajout_bien_immobilier_window.register(validate_input)
    global nombre_pieces_entry
    nombre_pieces_entry = tk.Entry(ajout_bien_immobilier_window, validate="key", validatecommand=(validate_func, "%P"))
    nombre_pieces_entry.grid(row=5, column=1, padx=10, pady=10)

    classe_energetique_label = tk.Label(ajout_bien_immobilier_window, text="Classe énergétique :")
    classe_energetique_label.grid(row=6, column=0, padx=10, pady=10, sticky=tk.W)
    global classe_energetique_var
    classe_energetique_var = tk.StringVar(ajout_bien_immobilier_window)
    classe_energetique_choices = ["A", "B", "C", "D", "E", "F", "G"]
    classe_energetique_var.set(classe_energetique_choices[0])

    classe_energetique_dropdown = tk.OptionMenu(ajout_bien_immobilier_window, classe_energetique_var, *classe_energetique_choices)
    classe_energetique_dropdown.grid(row=6, column=1, padx=10, pady=10, sticky=tk.W)

    annee_construction_label = tk.Label(ajout_bien_immobilier_window, text="Année de construction :")
    annee_construction_label.grid(row=7, column=0, padx=10, pady=10, sticky=tk.W)

    validate_func = ajout_bien_immobilier_window.register(validate_input)
    global annee_construction_entry
    annee_construction_entry = tk.Entry(ajout_bien_immobilier_window, validate="key", validatecommand=(validate_func, "%P"))
    annee_construction_entry.grid(row=7, column=1, padx=10, pady=10)

    # Création de boutons radios pour la nature de gestion
    nature_gestion_label = tk.Label(ajout_bien_immobilier_window, text="Nature de la gestion :")
    nature_gestion_label.grid(row=8, column=0, padx=10, pady=10, sticky=tk.W)

    global nature_gestion_value
    nature_gestion_value = tk.StringVar()
    nature_gestion_value.set("Location")  # Valeur par défaut sélectionnée

    location_radio = tk.Radiobutton(ajout_bien_immobilier_window, text="Location", variable=nature_gestion_value, value="Location")
    location_radio.grid(row=8, column=1, padx=10, pady=10, sticky=tk.W)

    vente_radio = tk.Radiobutton(ajout_bien_immobilier_window, text="Vente", variable=nature_gestion_value, value="Vente")
    vente_radio.grid(row=8, column=2, padx=10, pady=10, sticky=tk.W)

    #=====A METTRE AUTOMATIQUEMENT AVEC LOCAL.DATE EN SQL===#
    date_mise_marche_label = tk.Label(ajout_bien_immobilier_window, text="Date de mise en marche :")
    date_mise_marche_label.grid(row=9, column=0, padx=10, pady=10, sticky=tk.W)
    # Créer un label pour la date courante
    today_label = tk.Label(ajout_bien_immobilier_window, text=date.today().strftime("%d/%m/%Y"))
    today_label.grid(row=9, column=1, padx=10, pady=10, sticky=tk.E)
    #date_mise_marche_entry = tk.Entry(ajout_bien_immobilier_window)
    #date_mise_marche_entry.grid(row=8, column=1, padx=10, pady=10)

    prix_label = tk.Label(ajout_bien_immobilier_window, text="Prix :")
    prix_label.grid(row=10, column=0, padx=10, pady=10, sticky=tk.W)

    validate_func = ajout_bien_immobilier_window.register(validate_input)
    global prix_entry
    prix_entry = tk.Entry(ajout_bien_immobilier_window, validate="key", validatecommand=(validate_func, "%P"))
    prix_entry.grid(row=10, column=1, padx=10, pady=10)

    # Création du bouton de validation
    valider_button = tk.Button(ajout_bien_immobilier_window, text="Valider", command=valider_saisie)
    valider_button.grid(row=11, column=0, padx=10, pady=10)


#def recuperation_infos_bien(db_file):
#    # Connexion à la base de données
#    conn = sqlite3.connect('biens_immo.db')

    # Récupération des biens immobiliers
#    biens_immo = []
#    cursor = conn.execute('SELECT * FROM biens')
#    for row in cursor:
#        biens_immo.append(row)

    # Fermeture de la connexion
#    conn.close()

#Force l'utilisateur a entrer un nombre
def validate_input(new_value):
    if new_value == "":
        return True

    try:
        float(new_value)
        return True
    except ValueError:
        return False
    
def valider_saisie():
    """Récupère les valeurs saisies et les ajoute à la base de données"""

    # Récupération des valeurs saisies dans les champs de saisie
    type_immobilier = type_immobilier_value.get()
    nom_voie_adresse = adresse_nomvoie_entry.get()
    cp_adresse = cp_adresse_entry.get()
    type_voie_adresse = adresse_type_voie_var.get()
    nr_adresse = adresse_nr_entry.get()
    nom_ville_adresse = nom_ville_adresse_entry.get()
    adresse_sans_ville = "{} {} {}".format(nr_adresse,type_voie_adresse,nom_voie_adresse)
    ville_cp_adresse = "{} {}".format(cp_adresse,nom_ville_adresse)
    superficie_couvert = superficie_couvert_entry.get()
    superficie_jardin = superficie_jardin_entry.get()
    nombre_pieces = nombre_pieces_entry.get()
    classe_energetique = classe_energetique_var.get()
    annee_construction = annee_construction_entry.get()
    nature_gestion = nature_gestion_value.get()
    #date_mise_marche = date_mise_marche_entry.get()
    prix = prix_entry.get()
 
    # Création d'un dictionnaire avec les valeurs saisies
    bien = {
        'type_immobilier': type_immobilier,
        'adresse_sans_ville' : adresse_sans_ville,
        'ville_cp_adresse' : ville_cp_adresse,
        'nr_adresse' : nr_adresse,
        'type_voie_adresse' : type_voie_adresse,
        'nom_voie_adresse' : nom_voie_adresse,
        'cp_adresse' : cp_adresse,
        'nom_ville_adresse' : nom_ville_adresse,
        'superficie_couvert': superficie_couvert,
        'superficie_jardin': superficie_jardin,
        'nombre_pieces': nombre_pieces,
        'classe_energetique': classe_energetique,
        'annee_construction': annee_construction,
        'nature_gestion': nature_gestion,
        #'date_mise_marche': date_mise_marche,
        'prix': prix
    }

    # Ajout du bien immobilier dans la base de données
    inserer_bien_immobilier(db_file, bien)

    # Fermeture de la fenêtre d'ajout de bien immobilier
    ajout_bien_immobilier_window.destroy()
    print("test")


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

#Variables globales :


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

def closeSplash():
    splash_screen.destroy()

root.after(4000, closeSplash)  # Fermer la fenêtre de splash après 4 secondes
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

ajouter_bien_button = tk.Button(root, text="Ajouter un bien immobilier", command=ouvrir_ajout_bien_immobilier)
ajouter_bien_button.grid(row=0, column=0, padx=10, pady=10)

# Start the event loop
root.deiconify()
splash_screen.destroy()
root.mainloop()