import sqlite3
import pytest
from database import inserer_bien_immobilier, validate_input

TEST_DB = ":memory:"

# Le DDL pour créer la table, copié depuis main.create_database
TABLE_SCHEMA_DDL = """
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


@pytest.fixture
def db_connection():
    """Fixture to create an in-memory db connection with the schema applied."""
    conn = sqlite3.connect(TEST_DB)  # Crée une connexion à la base en mémoire
    cursor = conn.cursor()
    cursor.execute(TABLE_SCHEMA_DDL)  # Applique le schéma
    conn.commit()
    yield conn  # Fournit la connexion active aux tests
    conn.rollback()  # Nettoie les changements après le test


# Renommé pour refléter ce qu'il teste maintenant
def test_database_schema_applied(db_connection):
    """Test that the db schema (table) is correctly applied by the fixture."""
    cursor = db_connection.cursor()
    # Verify table exists
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
    tables = [row[0] for row in cursor.fetchall()]
    assert "biens_immobiliers" in tables


# E302: expected 2 blank lines, found 1
# E302: expected 2 blank lines, found 1
def test_inserer_bien_immobilier(db_connection):
    """Test property insertion"""
    test_property = {
        "type_immobilier": "Maison",
        "nr_adresse": "12",
        "type_voie_adresse": "Rue",
        "nom_voie_adresse": "des Fleurs",
        "cp_adresse": "75000",
        "nom_ville_adresse": "Paris",
        "rue_complete": "12 Rue des Fleurs",
        "superficie_couvert": "100",
        "superficie_jardin": "50",
        "nombre_pieces": "5",
        "classe_energetique": "A",
        "annee_construction": "2020",
        "nature_gestion": "Location",
        "date_mise_marche": "01/01/2023",
        "prix": "500000",
    }

    # Test direct de la fonction d'insertion avec la connexion existante
    inserer_bien_immobilier(None, test_property, conn=db_connection)

    # Vérification des données insérées
    cursor = db_connection.cursor()
    cursor.execute("SELECT * FROM biens_immobiliers")
    result = cursor.fetchone()
    assert result is not None
    assert result[1] == "Maison"
    assert result[4] == "des Fleurs"


# E302: expected 2 blank lines, found 1
@pytest.mark.parametrize(
    "input_value,expected",
    [
        ("123", True),
        ("45.67", True),
        ("", True),
        ("abc", False),
        ("12a3", False),
        ("45,67", False),
    ],
)
def test_validate_input(input_value, expected):
    """Test input validation"""
    assert validate_input(input_value) == expected
