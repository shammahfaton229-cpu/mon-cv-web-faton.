from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy 

# Importation pour les requêtes à la base de données
from sqlalchemy.orm import Session 

# CRUCIAL : Définissez explicitement le dossier static
app = Flask(__name__, static_folder='static') 

# --- Configuration de la Base de Données ---
# Utilisez l'URL de la base de données Render pour le déploiement final, 
# ou 'sqlite:///site.db' si vous faites un test local.
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
db = SQLAlchemy(app) 
# ---------------------------------------------


# --- DÉFINITION DES MODÈLES DE BASE DE DONNÉES (POUR LESQUELS VOS DONNÉES SONT DANS database.py) ---

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

# --- FIN DES MODÈLES ---


@app.route('/')
def index():
    # --- MODIFICATION CRITIQUE : RÉCUPÉRATION DES DONNÉES DE LA BDD ---
    with Session(db.engine) as session:
        # Récupère TOUS les objets de chaque modèle
        experiences_db = session.scalars(db.select(Experience)).all()
        educations_db = session.scalars(db.select(Education)).all()
        stages_db = session.scalars(db.select(Stage)).all()
        competences_db = session.scalars(db.select(Competence)).all()
    # ------------------------------------------------------------------

    # Les données de la BDD sont passées au template
    return render_template(
        'index.html',
        experiences=experiences_db, # Avant: experiences_data
        educations=educations_db,   # Avant: educations_data
        stages=stages_db,           # Avant: stages_data
        competences=competences_db  # Avant: competences_data
    )

if __name__ == '__main__':
    # Lancez l'application en mode debug
    app.run(debug=True)