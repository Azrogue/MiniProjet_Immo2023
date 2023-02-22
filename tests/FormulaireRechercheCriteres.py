import tkinter as tk

root = tk.Tk()
root.title("Recherche de biens")
root.geometry("800x600")

# Créer un label pour le titre de la page
title_label = tk.Label(root, text="Recherche de biens", font=("Helvetica", 20))
title_label.pack(pady=20)

# Créer un label pour la recherche par année de construction
year_label = tk.Label(root, text="Année de construction :")
year_label.pack()

year_min_label = tk.Label(root, text="Min")
year_min_label.pack()

year_min_entry = tk.Entry(root)
year_min_entry.pack()

year_max_label = tk.Label(root, text="Max")
year_max_label.pack()

year_max_entry = tk.Entry(root)
year_max_entry.pack()

# Créer un label pour la recherche par type de biens
type_label = tk.Label(root, text="Type de biens :")
type_label.pack()

type_entry = tk.Entry(root)
type_entry.pack()

# Créer un label pour la recherche par commune
commune_label = tk.Label(root, text="Commune :")
commune_label.pack()

commune_entry = tk.Entry(root)
commune_entry.pack()

# Créer un label pour la recherche par superficie couverte
surface_label = tk.Label(root, text="Superficie couverte :")
surface_label.pack()

surface_min_label = tk.Label(root, text="Min")
surface_min_label.pack()

surface_min_entry = tk.Entry(root)
surface_min_entry.pack()

surface_max_label = tk.Label(root, text="Max")
surface_max_label.pack()

surface_max_entry = tk.Entry(root)
surface_max_entry.pack()

# Créer un label pour la recherche par nature de la gestion
gestion_label = tk.Label(root, text="Nature de la gestion :")
gestion_label.pack()

gestion_entry = tk.Entry(root)
gestion_entry.pack()

# Créer un label pour la recherche par prix
prix_label = tk.Label(root, text="Prix :")
prix_label.pack()

prix_min_label = tk.Label(root, text="Min")
prix_min_label.pack()

prix_min_entry = tk.Entry(root)
prix_min_entry.pack()

prix_max_label = tk.Label(root, text="Max")
prix_max_label.pack()

prix_max_entry = tk.Entry(root)
prix_max_entry.pack()

# Créer un bouton pour lancer la recherche
search_button = tk.Button(root, text="Rechercher", bg="white", fg="black", font=("Helvetica", 14))
search_button.pack(pady=20)

root.mainloop()
