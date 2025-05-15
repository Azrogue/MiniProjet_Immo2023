import tkinter as tk
from tkinter import messagebox
from ttkthemes import ThemedStyle
import os
import sqlite3
import time
from tkinter import ttk

# ===================================
#              FONCTIONS
# ===================================
# Chemin de la base de données
db_file = "bien_immo.sqlite"

def create_database(db_file):  # création de la base de données
    """Crée une base de données SQLite avec une table 'biens_immobiliers'"""
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS biens_immobiliers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            type_immobilier TEXT,
            nr_adresse TEXT,
            type_voie_adresse TEXT,
            nom_voie_adresse TEXT,
            cp_adresse INTEGER,
            nom_ville_adresse TEXT,
            rue_complete TEXT,
            superficie_couvert REAL,
            superficie_jardin REAL,
            nombre_pieces INTEGER,
            classe_energetique TEXT,
            annee_construction INTEGER,
            nature_gestion TEXT,
            prix REAL,
            date_mise_marche TEXT,
            timestamp DATE DEFAULT (datetime('now','localtime'))
        )
        """
    )
    conn.commit()
    conn.close()

# Fonction qui ajoute les données dans la base de données

def inserer_bien_immobilier(db_file, bien):
    """Insère un bien immobilier dans la table 'biens_immobiliers' de la base de données SQLite"""
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    cursor.execute(
        """
        INSERT INTO biens_immobiliers (
            type_immobilier,
            nr_adresse,
            type_voie_adresse,
            nom_voie_adresse,
            cp_adresse,
            nom_ville_adresse,
            rue_complete,
            superficie_couvert,
            superficie_jardin,
            nombre_pieces,
            classe_energetique,
            annee_construction,
            nature_gestion,
            date_mise_marche,
            prix
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
        (
            bien['type_immobilier'],
            bien['nr_adresse'],
            bien['type_voie_adresse'],
            bien['nom_voie_adresse'],
            bien['cp_adresse'],
            bien['nom_ville_adresse'],
            bien['rue_complete'],
            bien['superficie_couvert'],
            bien['superficie_jardin'],
            bien['nombre_pieces'],
            bien['classe_energetique'],
            bien['annee_construction'],
            bien['nature_gestion'],
            bien['date_mise_marche'],
            bien['prix']
        )
    )
    conn.commit()
    conn.close()



def ouvrir_ajout_bien_immobilier():

    # Création de la fenêtre d'ajout de bien immobilier
    global ajout_bien_immobilier_window
    ajout_bien_immobilier_window = tk.Toplevel(root)
    ajout_bien_immobilier_window.title("Ajouter un bien immobilier")
    ajout_bien_immobilier_window.geometry("600x500")

    global type_immobilier_value
    type_immobilier_value = tk.StringVar(value="Maison")

    # Création des boutons radio pour le type d'immobilier
    type_immobilier_label = tk.Label(ajout_bien_immobilier_window, text="Type d'immobilier :")
    type_immobilier_label.grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)

    type_immobilier_maison_radio = tk.Radiobutton(
        ajout_bien_immobilier_window,
        text="Maison",
        variable=type_immobilier_value,
        value="Maison",command=lambda: superficie_jardin_entry.grid()
    )
    type_immobilier_maison_radio.grid(row=0, column=1, padx=10, pady=10, sticky=tk.W)

    type_immobilier_appartement_radio = tk.Radiobutton(
        ajout_bien_immobilier_window,
        text="Appartement",
        variable=type_immobilier_value,
        value="Appartement",command=lambda: superficie_jardin_entry.grid_remove()
    )
    type_immobilier_appartement_radio.grid(row=0, column=2, padx=10, pady=10)

    #création de l'adresse avec les champs demandés
    adresse_label = tk.Label(ajout_bien_immobilier_window, text="Adresse :")
    adresse_label.grid(row=1, column=0, padx=10, pady=10, sticky=tk.W)

    adresse_nr_label = tk.Label(ajout_bien_immobilier_window, text="N°:")
    adresse_nr_label.place(x=170, y=55)
    global adresse_nr_entry
    adresse_nr_entry = tk.Entry(ajout_bien_immobilier_window, width=5)
    adresse_nr_entry.place(x=192, y=55)
    
    adresse_type_voie_label = tk.Label(ajout_bien_immobilier_window, text="Type de voie:")
    adresse_type_voie_label.place(x=225, y=55)
    global adresse_type_voie_var
    adresse_type_voie_var = tk.StringVar(ajout_bien_immobilier_window)
    addresse_type_voie_choices = ["Rue", "Allée", "Boulevard", "Chemin"]
    adresse_type_voie_var.set(addresse_type_voie_choices[0])

    adresse_type_voie_dropdown = tk.OptionMenu(ajout_bien_immobilier_window, adresse_type_voie_var, *addresse_type_voie_choices)
    adresse_type_voie_dropdown.place(x=298, y=50)
    
    adresse_nomvoie_label = tk.Label(ajout_bien_immobilier_window, text="Nom de la voie:")
    adresse_nomvoie_label.place(x=375, y=55)
    global adresse_nomvoie_entry
    adresse_nomvoie_entry = tk.Entry(ajout_bien_immobilier_window, width=15)
    adresse_nomvoie_entry.place(x=463, y=55)

    cp_adresse_label = tk.Label(ajout_bien_immobilier_window, text="Code postale:")
    cp_adresse_label.grid(row=2, column=1, padx=10, pady=10, sticky=tk.W)
    global cp_adresse_entry
    cp_adresse_entry = tk.Entry(ajout_bien_immobilier_window, width=7)
    cp_adresse_entry.place(x=250, y=97)

    nom_ville_adresse_label = tk.Label(ajout_bien_immobilier_window, text="Ville :")
    nom_ville_adresse_label.grid(row=2, column=2, padx=10, pady=10, sticky=tk.W)
    global nom_ville_adresse_entry
    nom_ville_adresse_entry = tk.Entry(ajout_bien_immobilier_window,width= 15)
    nom_ville_adresse_entry.place(x=350, y=97)

    #création de l'entrée pour la superficie
    superficie_couvert_label = tk.Label(ajout_bien_immobilier_window, text="Superficie couverte (m²) :")
    superficie_couvert_label.grid(row=3, column=0, padx=10, pady=10, sticky=tk.W)

    validate_func = ajout_bien_immobilier_window.register(validate_input)
    global superficie_couvert_entry
    superficie_couvert_entry = tk.Entry(ajout_bien_immobilier_window, validate="key", validatecommand=(validate_func, "%P"))
    superficie_couvert_entry.grid(row=3, column=1, padx=10, pady=10)

    #superficie avec jardin visible seulement quand le type "maison est choisi"
    superficie_jardin_label = tk.Label(ajout_bien_immobilier_window, text="Superficie jardin (m²) :")
    superficie_jardin_label.grid(row=4, column=0, padx=10, pady=10, sticky=tk.W)
    validate_func = ajout_bien_immobilier_window.register(validate_input)
    global superficie_jardin_entry
    superficie_jardin_entry = tk.Entry(ajout_bien_immobilier_window, validate="key", validatecommand=(validate_func, "%P"))
    superficie_jardin_entry.grid(row=4, column=1, padx=10, pady=10)

    # ajout nombre de pieces
    nombre_pieces_label = tk.Label(ajout_bien_immobilier_window, text="Nombre de pièces :")
    nombre_pieces_label.grid(row=5, column=0, padx=10, pady=10, sticky=tk.W)
    validate_func = ajout_bien_immobilier_window.register(validate_input)
    global nombre_pieces_entry
    nombre_pieces_entry = tk.Entry(ajout_bien_immobilier_window, validate="key", validatecommand=(validate_func, "%P"))
    nombre_pieces_entry.grid(row=5, column=1, padx=10, pady=10)

    #choix de la classe energetique sous forme de liste deroulante
    classe_energetique_label = tk.Label(ajout_bien_immobilier_window, text="Classe énergétique :")
    classe_energetique_label.grid(row=6, column=0, padx=10, pady=10, sticky=tk.W)
    global classe_energetique_var
    classe_energetique_var = tk.StringVar(ajout_bien_immobilier_window)
    classe_energetique_choices = ["A", "B", "C", "D", "E", "F", "G"]
    classe_energetique_var.set(classe_energetique_choices[0])
    classe_energetique_dropdown = tk.OptionMenu(ajout_bien_immobilier_window, classe_energetique_var, *classe_energetique_choices)
    classe_energetique_dropdown.grid(row=6, column=1, padx=10, pady=10, sticky=tk.W)

    # ajout de l'année de cnstruction sous forme d'entrée
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

    # ajout de la date de mise en marche sous forme de spinbox
    date_mise_marche_label = tk.Label(ajout_bien_immobilier_window, text="Date de mise en marche :")
    date_mise_marche_label.grid(row=9, column=0, padx=10, pady=10, sticky=tk.W)
    # Créer un label pour la date courante
    global day_spinbox_value
    day_spinbox_value = tk.Spinbox(ajout_bien_immobilier_window, from_=1, to=31, width=2)
    day_spinbox_value.place(x=170, y=400)

    global month_spinbox_value
    month_spinbox_value = tk.Spinbox(ajout_bien_immobilier_window, from_=1, to=12, width=2)
    month_spinbox_value.place(x=200, y=400)

    global year_spinbox_value
    year_spinbox_value = tk.Spinbox(ajout_bien_immobilier_window, from_=1800, to=2023, width=4)
    year_spinbox_value.place(x=230, y=400)

    # ajout du prix sous forme d'entrée
    prix_label = tk.Label(ajout_bien_immobilier_window, text="Prix :")
    prix_label.grid(row=10, column=0, padx=10, pady=10, sticky=tk.W)
    validate_func = ajout_bien_immobilier_window.register(validate_input)
    global prix_entry
    prix_entry = tk.Entry(ajout_bien_immobilier_window, validate="key", validatecommand=(validate_func, "%P"))
    prix_entry.grid(row=10, column=1, padx=10, pady=10)
    
    # Création du bouton de validation
    valider_button = tk.Button(ajout_bien_immobilier_window, text="Valider", command=valider_saisie)
    valider_button.grid(row=12, column=0, padx=10, pady=10)

def recup_data_in_db():
    # Connexion à la base de données
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()

    # Récupérer les données de la table biens_immobiliers
    cursor.execute("SELECT ID, type_immobilier, rue_complete, cp_adresse, nom_ville_adresse, superficie_couvert, superficie_jardin, nombre_pieces, classe_energetique, annee_construction, nature_gestion, prix, timestamp FROM biens_immobiliers")
    data = cursor.fetchall()
    
    # Fermer la connexion à la base de données
    cursor.close()
    conn.close()
    return data

def insertion_donnee_tableau():
    global data
    data = recup_data_in_db()
    for row in data:
        table.insert('', 'end', values=row)

#==============tabloooo================
def tableau_infos_bien():
    # data = recup_data_in_db() # Inutile, insertion_donnee_tableau le fait déjà

    # Créer le tableau avec les données
    global table
    table = ttk.Treeview(root)
    table['columns'] = ['ID', 'type_immobilier', 'rue_complete',
                        'cp_adresse', 'nom_ville_adresse', 'superficie_couvert', 'superficie_jardin',
                        'nombre_pieces', 'classe_energetique', 'annee_construction', 'nature_gestion',
                        'prix', 'timestamp'] # E231: 'prix','timestamp'] -> 'prix', 'timestamp']
    table['show'] = 'headings'
    
    for column in table['columns']:
        table.heading(column, text=column)
        

    insertion_donnee_tableau()

    table.pack()
    
    
    # Définir des largeurs par défaut pour certaines colonnes
    
    table.column('ID', width=50, minwidth=50)
    table.column('rue_complete', width=80, minwidth=50)
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

def update_table():
    # Effacer les données actuelles du Treeview
    table.delete(*table.get_children())

    # Récupérer les valeurs des champs de saisie et des cases à cocher
    annee_construction_value = annee_construction_entry.get()
    vente_value = vente_var.get()
    location_value = location_var.get()
    ville_value = ville_entry.get()
    appartement_value = appartement_var.get()
    maison_value = maison_var.get()
    prix_min_value = prix_min_entry.get()
    prix_max_value = prix_max_entry.get()
    superficie_min_value = superficie_min_entry.get()
    superficie_max_value = superficie_max_entry.get()

    # Filtrer les données de la base de données en fonction des choix de l'utilisateur
    filtered_data = []
    for row in data:
        # Exemple de filtrage simple (à adapter selon vos besoins)
        if annee_construction_value and str(row[9]) != annee_construction_value:
            continue
        if ville_value and ville_value.lower() not in str(row[4]).lower():
            continue
        if vente_value and row[10] != 'Vente':
            continue
        if location_value and row[10] != 'Location':
            continue
        if appartement_value and row[1] != 'Appartement':
            continue
        if maison_value and row[1] != 'Maison':
            continue
        if prix_min_value and float(row[11]) < float(prix_min_value):
            continue
        if prix_max_value and float(row[11]) > float(prix_max_value):
            continue
        if superficie_min_value and float(row[5]) < float(superficie_min_value):
            continue
        if superficie_max_value and float(row[5]) > float(superficie_max_value):
            continue
        filtered_data.append(row)

    # Insérer les données filtrées dans le Treeview
    for row in filtered_data:
        table.insert('', 'end', values=row)

def actualiser_tableau():
    # Connexion à la base de données
    # data = recup_data_in_db() # Inutile, insertion_donnee_tableau le fait déjà

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
    type_immobilier = type_immobilier_value.get()
    nom_voie_adresse = adresse_nomvoie_entry.get()
    cp_adresse = cp_adresse_entry.get()
    type_voie_adresse = adresse_type_voie_var.get()
    nr_adresse = adresse_nr_entry.get()
    nom_ville_adresse = nom_ville_adresse_entry.get()
    rue_complete = f"{nr_adresse} {type_voie_adresse} {nom_voie_adresse}"
    superficie_couvert = superficie_couvert_entry.get()
    superficie_jardin = superficie_jardin_entry.get()
    nombre_pieces = nombre_pieces_entry.get()
    classe_energetique = classe_energetique_var.get()
    annee_construction = annee_construction_entry.get()
    nature_gestion = nature_gestion_value.get()
    date_mise_marche = f"{day_spinbox_value.get()}/{month_spinbox_value.get()}/{year_spinbox_value.get()}"
    prix = prix_entry.get()
    bien = {
        'type_immobilier': type_immobilier,
        'nr_adresse': nr_adresse,
        'type_voie_adresse': type_voie_adresse,
        'nom_voie_adresse': nom_voie_adresse,
        'cp_adresse': cp_adresse,
        'nom_ville_adresse': nom_ville_adresse,
        'rue_complete': rue_complete,
        'superficie_couvert': superficie_couvert,
        'superficie_jardin': superficie_jardin,
        'nombre_pieces': nombre_pieces,
        'classe_energetique': classe_energetique,
        'annee_construction': annee_construction,
        'nature_gestion': nature_gestion,
        'date_mise_marche': date_mise_marche,
        'prix': prix
    }
    inserer_bien_immobilier(db_file, bien)
    ajout_bien_immobilier_window.destroy()
    actualiser_tableau()

def centerWindow(width, height, root):
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = int((screen_width / 2) - (width / 2))
    y = int((screen_height / 2) - (height / 2))
    return x, y

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
        id_list.insert(tk.END, (bien[0], bien[2], bien[4]))

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
style = ThemedStyle(root)
style.set_theme("yaru") #plastik , 


# Titre de la fenêtre
root.title("Gestion Immobilière")

# SPLASH SCREEN CODE
splash_screen = tk.Toplevel(background="white")
splash_screen.overrideredirect(True)
splash_screen.title("Splash Screen")
x, y = centerWindow(600, 400, root)
splash_screen.geometry(f"600x400+{x}+{y}") # E251: image = image -> image=image
image = tk.PhotoImage(file="Assets/img/splash.png")
label = tk.Label(splash_screen, image=image)
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

# Fonction pour fermer le splash screen

def closeSplash():
    splash_screen.destroy()

root.after(4000, closeSplash)  # Fermer la fenêtre de splash après 4 secondes
time.sleep(4)

# Vérification de l'existence de la base de données
if not os.path.isfile(db_file):
    if messagebox.askyesno("Créer la base de données", "La base de données n'existe pas encore, voulez-vous la créer ?"):
        create_database(db_file)
    else:
        root.destroy()

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
# ==================Filters==================
# Créer un frame à gauche du tableau pour les filtres
filters_frame = ttk.Frame(root)
filters_frame.pack(side=tk.LEFT, padx=10, pady=10)

# Ajouter un champ de saisie pour le code postal
annee_construction_label = tk.Label(filters_frame, text="Année de construction:")
annee_construction_label.pack()
annee_construction_entry = tk.Entry(filters_frame)
annee_construction_entry.pack()
# Ajouter un champ de saisie pour la ville
ville_label = tk.Label(filters_frame, text="Ville:")
ville_label.pack()
ville_entry = tk.Entry(filters_frame)
ville_entry.pack()
# Ajouter deux cases à cocher pour la nature de la gestion
vente_var = tk.IntVar()
location_var = tk.IntVar()
appartement_var = tk.IntVar()
maison_var = tk.IntVar()
gestion_label = tk.Label(filters_frame, text="Nature de la gestion:")
gestion_label.pack()
vente_checkbox = tk.Checkbutton(filters_frame, text="Vente", variable=vente_var)
vente_checkbox.pack()
location_checkbox = tk.Checkbutton(filters_frame, text="Location", variable=location_var)
location_checkbox.pack()
# Ajouter deux cases à cocher pour le type de bien
type_immobilier_label = tk.Label(filters_frame, text="Type de bien:")
type_immobilier_label.pack()
appartement_checkbox = tk.Checkbutton(filters_frame, text="Appartement", variable=appartement_var)
appartement_checkbox.pack()
maison_checkbox = tk.Checkbutton(filters_frame, text="Maison", variable=maison_var)
maison_checkbox.pack()

#change la position des filtres suivants
filters_frame_right = ttk.Frame(root)
filters_frame_right.pack()

# ajoute deux champs pour choisir le prix maximum et minimum
prix_min_label = tk.Label(filters_frame_right, text="Prix min:")
prix_min_label.pack()
prix_min_entry = tk.Entry(filters_frame_right)
prix_min_entry.pack()
prix_max_label = tk.Label(filters_frame_right, text="Prix max:")
prix_max_label.pack()
prix_max_entry = tk.Entry(filters_frame_right)
prix_max_entry.pack()
# ajoute deux champs pour choisir la superficie maximum et minimum
superficie_min_label = tk.Label(filters_frame_right, text="superficie min:")
superficie_min_label.pack()
superficie_min_entry = tk.Entry(filters_frame_right)
superficie_min_entry.pack()
superficie_max_label = tk.Label(filters_frame_right, text="superficie max:")
superficie_max_label.pack()
superficie_max_entry = tk.Entry(filters_frame_right)
superficie_max_entry.pack()

#actualise la page en fonction des choix faits
annee_construction_entry.bind("<KeyRelease>", lambda event: update_table())
vente_checkbox.config(command=update_table)
location_checkbox.config(command=update_table)
appartement_checkbox.config(command=update_table)
maison_checkbox.config(command=update_table)
prix_max_entry.bind("<KeyRelease>", lambda event: update_table())
prix_min_entry.bind("<KeyRelease>", lambda event: update_table())
superficie_max_entry.bind("<KeyRelease>", lambda event: update_table())
superficie_min_entry.bind("<KeyRelease>", lambda event: update_table())

#actualise la page en fonction des choix faits mais avec les autre choix possibles
ville_entry.bind("<KeyRelease>", lambda event: update_table())
vente_checkbox.config(command=update_table)
location_checkbox.config(command=update_table)
maison_checkbox.config(command=update_table)
appartement_checkbox.config(command=update_table)
prix_min_entry.bind("<KeyRelease>", lambda event: update_table())
prix_max_entry.bind("<KeyRelease>", lambda event: update_table())
superficie_min_entry.bind("<KeyRelease>", lambda event: update_table())
superficie_max_entry.bind("<KeyRelease>", lambda event: update_table())

# Start the event loop
root.deiconify()
root.mainloop()
