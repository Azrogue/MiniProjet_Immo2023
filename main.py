import tkinter as tk
import tkinter.ttk as ttk
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
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?,?,?,?,?)
    """, (
        bien['type_immobilier'],
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
    ajout_bien_immobilier_window.geometry("500x500")

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
    adresse_nr_entry.place(x=170, y=55)
    
    global adresse_type_voie_var
    adresse_type_voie_var = tk.StringVar(ajout_bien_immobilier_window)
    addresse_type_voie_choices = ["Rue", "Allée", "Boulevard", "Chemin"]
    adresse_type_voie_var.set(addresse_type_voie_choices[0])

    adresse_type_voie_dropdown = tk.OptionMenu(ajout_bien_immobilier_window, adresse_type_voie_var, *addresse_type_voie_choices)
    adresse_type_voie_dropdown.place(x=202, y=47)
    
    global adresse_nomvoie_entry
    adresse_nomvoie_entry = tk.Entry(ajout_bien_immobilier_window, width=8)
    adresse_nomvoie_entry.place(x=262, y=55)

    global cp_adresse_entry
    cp_adresse_entry = tk.Entry(ajout_bien_immobilier_window, width=6)
    cp_adresse_entry.place(x=280, y=55)

    global nom_ville_adresse_entry
    nom_ville_adresse_entry = tk.Entry(ajout_bien_immobilier_window,width= 8)
    nom_ville_adresse_entry.place(x=302, y=55)
    superficie_couvert_label = tk.Label(ajout_bien_immobilier_window, text="Superficie couverte (m²) :")
    superficie_couvert_label.grid(row=2, column=0, padx=10, pady=10, sticky=tk.W)

    validate_func = ajout_bien_immobilier_window.register(validate_input)
    global superficie_couvert_entry
    superficie_couvert_entry = tk.Entry(ajout_bien_immobilier_window, validate="key", validatecommand=(validate_func, "%P"))
    superficie_couvert_entry.grid(row=2, column=1, padx=10, pady=10)

    superficie_jardin_label = tk.Label(ajout_bien_immobilier_window, text="Superficie jardin (m²) :")
    superficie_jardin_label.grid(row=3, column=0, padx=10, pady=10, sticky=tk.W)

    validate_func = ajout_bien_immobilier_window.register(validate_input)
    global superficie_jardin_entry
    superficie_jardin_entry = tk.Entry(ajout_bien_immobilier_window, validate="key", validatecommand=(validate_func, "%P"))
    superficie_jardin_entry.grid(row=3, column=1, padx=10, pady=10)

    nombre_pieces_label = tk.Label(ajout_bien_immobilier_window, text="Nombre de pièces :")
    nombre_pieces_label.grid(row=4, column=0, padx=10, pady=10, sticky=tk.W)

    validate_func = ajout_bien_immobilier_window.register(validate_input)
    global nombre_pieces_entry
    nombre_pieces_entry = tk.Entry(ajout_bien_immobilier_window, validate="key", validatecommand=(validate_func, "%P"))
    nombre_pieces_entry.grid(row=4, column=1, padx=10, pady=10)

    classe_energetique_label = tk.Label(ajout_bien_immobilier_window, text="Classe énergétique :")
    classe_energetique_label.grid(row=5, column=0, padx=10, pady=10, sticky=tk.W)
    global classe_energetique_var
    classe_energetique_var = tk.StringVar(ajout_bien_immobilier_window)
    classe_energetique_choices = ["A", "B", "C", "D", "E", "F", "G"]
    classe_energetique_var.set(classe_energetique_choices[0])

    classe_energetique_dropdown = tk.OptionMenu(ajout_bien_immobilier_window, classe_energetique_var, *classe_energetique_choices)
    classe_energetique_dropdown.grid(row=5, column=1, padx=10, pady=10, sticky=tk.W)

    annee_construction_label = tk.Label(ajout_bien_immobilier_window, text="Année de construction :")
    annee_construction_label.grid(row=6, column=0, padx=10, pady=10, sticky=tk.W)

    validate_func = ajout_bien_immobilier_window.register(validate_input)
    global annee_construction_entry
    annee_construction_entry = tk.Entry(ajout_bien_immobilier_window, validate="key", validatecommand=(validate_func, "%P"))
    annee_construction_entry.grid(row=6, column=1, padx=10, pady=10)

    # Création de boutons radios pour la nature de gestion
    nature_gestion_label = tk.Label(ajout_bien_immobilier_window, text="Nature de la gestion :")
    nature_gestion_label.grid(row=7, column=0, padx=10, pady=10, sticky=tk.W)

    global nature_gestion_value
    nature_gestion_value = tk.StringVar()
    nature_gestion_value.set("Location")  # Valeur par défaut sélectionnée

    location_radio = tk.Radiobutton(ajout_bien_immobilier_window, text="Location", variable=nature_gestion_value, value="Location")
    location_radio.grid(row=7, column=1, padx=10, pady=10, sticky=tk.W)

    vente_radio = tk.Radiobutton(ajout_bien_immobilier_window, text="Vente", variable=nature_gestion_value, value="Vente")
    vente_radio.grid(row=7, column=2, padx=10, pady=10, sticky=tk.W)

    #=====A METTRE AUTOMATIQUEMENT AVEC LOCAL.DATE EN SQL===#
    date_mise_marche_label = tk.Label(ajout_bien_immobilier_window, text="Date de mise en marche :")
    date_mise_marche_label.grid(row=8, column=0, padx=10, pady=10, sticky=tk.W)
    # Créer un label pour la date courante
    today_label = tk.Label(ajout_bien_immobilier_window, text=date.today().strftime("%d/%m/%Y"))
    today_label.grid(row=8, column=1, padx=10, pady=10, sticky=tk.E)
    #date_mise_marche_entry = tk.Entry(ajout_bien_immobilier_window)
    #date_mise_marche_entry.grid(row=8, column=1, padx=10, pady=10)

    prix_label = tk.Label(ajout_bien_immobilier_window, text="Prix :")
    prix_label.grid(row=9, column=0, padx=10, pady=10, sticky=tk.W)

    validate_func = ajout_bien_immobilier_window.register(validate_input)
    global prix_entry
    prix_entry = tk.Entry(ajout_bien_immobilier_window, validate="key", validatecommand=(validate_func, "%P"))
    prix_entry.grid(row=9, column=1, padx=10, pady=10)

    # Création du bouton de validation
    valider_button = tk.Button(ajout_bien_immobilier_window, text="Valider", command=valider_saisie)
    valider_button.grid(row=10, column=0, padx=10, pady=10)

def recup_data_in_db():
    # Connexion à la base de données
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()

    # Récupérer les données de la table biens_immobiliers
    cursor.execute("SELECT * FROM biens_immobiliers")
    data = cursor.fetchall()
    return data

    # Fermer la connexion à la base de données
    cursor.close()
    conn.close()

def insertion_donnee_tableau():
    global data
    data = recup_data_in_db()
    for row in data:
        row = list(row)
        del row[13]  # Supprimer la colonne 'date_mise_marche' (l'indice de la colonne est 13)
        table.insert('', tk.END, values=row)

#==============tabloooo================
def tableau_infos_bien():
    data = recup_data_in_db()

    # Créer le tableau avec les données
    global table
    table = ttk.Treeview(root)
    table['columns'] = ['ID', 'type_immobilier', 'nr_adresse', 'type_voie_adresse', 'nom_voie_adresse',
                        'cp_adresse', 'nom_ville_adresse', 'superficie_couvert', 'superficie_jardin',
                        'nombre_pieces', 'classe_energetique', 'annee_construction', 'nature_gestion',
                        'prix', 'timestamp']
    table['show'] = 'headings'
    for column in table['columns']:
        if column != 'date_mise_marche':
            table.heading(column, text=column)

    insertion_donnee_tableau()

    table.pack()

    # Définir des largeurs par défaut pour certaines colonnes
    
    table.column('ID', width=50, minwidth=50)
    table.column('nr_adresse', width=80, minwidth=50)
    table.column('superficie_couvert', width=50, minwidth=50)
    table.column('superficie_jardin', width=50, minwidth=50)
    table.column('nombre_pieces', width=50, minwidth=50)
    table.column('classe_energetique', width=50, minwidth=50)

    # Ajouter les scrollbar verticale et horizontale
    scrollbar_y = ttk.Scrollbar(root, orient=tk.VERTICAL, command=table.yview)
    scrollbar_y.pack(side=tk.RIGHT, fill=tk.Y)
    scrollbar_x = ttk.Scrollbar(root, orient=tk.HORIZONTAL, command=table.xview)
    scrollbar_x.pack(side=tk.BOTTOM, fill=tk.X)
    table.configure(yscrollcommand=scrollbar_y.set, xscrollcommand=scrollbar_x.set)

    

def actualiser_tableau():
    # Connexion à la base de données
    data = recup_data_in_db()

    # Effacer le contenu actuel du tableau
    table = root.children['!treeview']
    table.delete(*table.get_children())
    # Réinsérer les nouvelles données
    insertion_donnee_tableau()


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
    actualiser_tableau()


def centerWindow(width, height, root):  # Return 4 values needed to center Window
    screen_width = root.winfo_screenwidth()  # Width of the screen
    screen_height = root.winfo_screenheight() # Height of the screen     
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    return int(x), int(y)

def ouvrir_suppression_bien_immobilier():
    suppression_bien_window = tk.Toplevel(root)
    suppression_bien_window.title("Suppression de bien immobilier")

    # Créer une boîte de liste pour afficher les biens immobiliers existants
    id_list = tk.Listbox(suppression_bien_window)
    id_list.pack(fill=tk.BOTH, expand=1)

    # Ajouter un bouton "Sélectionner tout"
    select_all_button = tk.Button(suppression_bien_window, text="Sélectionner tout", command=lambda: id_list.select_set(0, tk.END))
    select_all_button.pack(side=tk.LEFT)

    # Ajouter un bouton "Désélectionner tout"
    deselect_all_button = tk.Button(suppression_bien_window, text="Désélectionner tout", command=lambda: id_list.selection_clear(0, tk.END))
    deselect_all_button.pack(side=tk.LEFT)

    # Ajouter un bouton "Supprimer"
    delete_button = tk.Button(suppression_bien_window, text="Supprimer", command=lambda: supprimer_biens_selectionnes(id_list.curselection()))
    delete_button.pack(side=tk.RIGHT)

    # Récupérer les données de la table biens_immobiliers
    data = recup_data_in_db()

    # Mettre à jour la liste des biens immobiliers dans la Listbox
    id_list.delete(0, tk.END)
    for bien in data:
        id_list.insert(tk.END, (bien[0], bien[4], bien[6]))

def supprimer_biens_selectionnes(selection):
    if not selection:
        messagebox.showwarning("Aucune sélection", "Veuillez sélectionner au moins un bien immobilier à supprimer.")
        return

    confirmation = messagebox.askyesno("Confirmation de suppression", "Êtes-vous sûr de vouloir supprimer les biens immobiliers sélectionnés ?")
    if not confirmation:
        return
    
    # Connexion à la base de données
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()

    # Récupérer les données de la table biens_immobiliers
    cursor.execute("SELECT * FROM biens_immobiliers")
    data = cursor.fetchall()

    # Supprimer les biens sélectionnés de la table biens_immobiliers
    for index in selection[::-1]:
        id_bien = data[index][0]
        cursor.execute("DELETE FROM biens_immobiliers WHERE ID=?", (id_bien,))
        conn.commit()

    # Fermer la connexion à la base de données
    cursor.close()
    conn.close()

    # Mettre à jour la liste des biens immobiliers dans la Listbox
    suppression_bien_window = tk.Toplevel(root)
    suppression_bien_window.title("Suppression de biens immobiliers")

    id_list = tk.Listbox(suppression_bien_window, width=30)
    id_list.grid(row=0, column=0, padx=10, pady=10)

    for bien in data:
        id_list.insert(tk.END, (bien[0], bien[4], bien[6]))

    # Afficher un message de confirmation
    messagebox.showinfo("Suppression réussie", "Les biens immobiliers sélectionnés ont été supprimés avec succès.")

    # Fermer la fenêtre
    suppression_bien_window.destroy()
    actualiser_tableau()



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

#ajouter_bien_button = tk.Button(root, text="Ajouter un bien immobilier", command=ouvrir_ajout_bien_immobilier)
#ajouter_bien_button.grid(row=0, column=0, padx=10, pady=10)

bouton_cadre = tk.Frame(root)
bouton_cadre.pack(side=tk.TOP, anchor=tk.NE)

# Bouton pour ajouter un bien immobilier
ajouter_bien_button = tk.Button(bouton_cadre, text="Ajouter un bien immobilier", command=ouvrir_ajout_bien_immobilier)
ajouter_bien_button.pack(side=tk.RIGHT)

# Bouton pour supprimer un bien immobilier
supprimer_bien_button = tk.Button(bouton_cadre, text="Suppression de biens", command=ouvrir_suppression_bien_immobilier)
supprimer_bien_button.pack(side=tk.RIGHT)

tableau_infos_bien()


# Start the event loop
root.deiconify()
root.mainloop()