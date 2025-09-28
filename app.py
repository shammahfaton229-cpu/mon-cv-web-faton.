from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy 
from typing import List, Dict # Importation pour les types de données

# CRUCIAL : Définissez explicitement le dossier static
app = Flask(__name__, static_folder='static') 

# --- Configuration de la Base de Données ---
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
db = SQLAlchemy(app) 
# ---------------------------------------------


# --- AJOUT CRITIQUE : DÉFINITION DES MODÈLES DE BASE DE DONNÉES ---

# Modèle pour les Études Universitaires/Expériences
class Experience(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    poste = db.Column(db.String(100), nullable=False)
    entreprise = db.Column(db.String(100), nullable=False)
    periode = db.Column(db.String(50), nullable=False)
    description = db.Column(db.Text)

# Modèle pour les Compétences
class Competence(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(100), nullable=False)
    niveau = db.Column(db.String(50), nullable=False)

# Modèle pour les Études (Primaires/Secondaires)
class Education(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    etablissement = db.Column(db.String(100), nullable=False)
    niveau = db.Column(db.String(50), nullable=False)
    periode = db.Column(db.String(50), nullable=False)
    diplome = db.Column(db.String(100))

# Modèle pour les Stages et Formations
class Stage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cadre = db.Column(db.String(100), nullable=False)
    centre = db.Column(db.String(100), nullable=False)
    annee = db.Column(db.String(20), nullable=False)
    diplome = db.Column(db.String(100))

# --- FIN DE L'AJOUT CRITIQUE ---


# --- Vos listes de données sont conservées pour l'affichage ---
# Note : Ces listes sont utilisées pour l'affichage *temporaire* car vous ne faites pas de requête à la BDD.
experiences_data: List[Dict[str, str]] = [
    {'poste': 'Étudiant en Licence 1', 'entreprise': 'Ecole Polytechnique d\'Abomey-Calavi (EPAC)', 'periode': '2023 - Aujourd\'hui', 'description': "Formation d'Ingénieur en Génie Electrique et Informatique Industrielle (GEII)."},
]
educations_data: List[Dict[str, str]] = [
    {'etablissement': 'Lycée Technique d\'Azowlisse', 'niveau': 'Secondaire', 'periode': '2019-2023', 'diplome': 'Baccalauréat Série C'},
]
stages_data: List[Dict[str, str]] = [
    {'cadre': 'Stage d\'initiation', 'centre': 'Entreprise locale de maintenance', 'annee': '2024'},
]
competences_data: List[Dict[str, str]] = [
    {'nom': 'Python', 'niveau': 'Débutant/Intermédiaire'},
    {'nom': 'HTML & CSS', 'niveau': 'Intermédiaire'},
]
# -----------------------------------------------------------


@app.route('/')
def index():
    # Ici, nous utilisons les listes de données temporaires pour l'affichage
    return render_template(
        'index.html',
        experiences=experiences_data,
        educations=educations_data,
        stages=stages_data,
        competences=competences_data
    )

if __name__ == '__main__':
    # Lancez l'application en mode debug
    app.run(debug=True)