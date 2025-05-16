import sqlite3

def create_database(db_path):
    """Create the database schema"""
    conn = sqlite3.connect(db_path)
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
    """)
    
    conn.commit()
    if should_close:
        conn.close()

def inserer_bien_immobilier(db_path, bien_data, conn=None):
    """Insert a property into the database"""
    should_close = False
    if conn is None:
        conn = sqlite3.connect(db_path)
        should_close = True
    
    cursor = conn.cursor()
    
    cursor.execute("""
        INSERT INTO biens_immobiliers (
            type_immobilier, nr_adresse, type_voie_adresse, 
            nom_voie_adresse, cp_adresse, nom_ville_adresse,
            rue_complete, superficie_couvert, superficie_jardin,
            nombre_pieces, classe_energetique, annee_construction,
            nature_gestion, prix, date_mise_marche
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        bien_data["type_immobilier"],
        bien_data["nr_adresse"],
        bien_data["type_voie_adresse"],
        bien_data["nom_voie_adresse"],
        bien_data["cp_adresse"],
        bien_data["nom_ville_adresse"],
        bien_data["rue_complete"],
        bien_data["superficie_couvert"],
        bien_data["superficie_jardin"],
        bien_data["nombre_pieces"],
        bien_data["classe_energetique"],
        bien_data["annee_construction"],
        bien_data["nature_gestion"],
        bien_data["prix"],
        bien_data["date_mise_marche"]
    ))
    
    conn.commit()

def validate_input(input_value):
    """Validate numeric input"""
    if not input_value:
        return True
    try:
        float(input_value)
        return True
    except ValueError:
        return False
