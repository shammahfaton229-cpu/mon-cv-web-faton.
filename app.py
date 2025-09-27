from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
import os
from sqlalchemy import asc, desc # Importe les fonctions de tri

# NOUVEAU: Importation de la fonction de création de DB
from database import create_database 

# Configuration de l'application Flask
app = Flask(__name__)
# Connexion à la base de données
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cv_data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# CORRECTION MAJEURE POUR RENDER : Crée la DB dans le contexte de l'application
# Ceci garantit que la base de données SQLite est créée et remplie 
# la première fois que Render lance Gunicorn.
with app.app_context():
    create_database()

# ----------------------------------------------------
# DÉFINITION DES MODÈLES (CLASSES)
# ----------------------------------------------------

class Experience(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    poste = db.Column(db.String(120), nullable=False)
    entreprise = db.Column(db.String(120), nullable=False)
    periode = db.Column(db.String(80), nullable=False)
    description = db.Column(db.Text, nullable=False)

class Competence(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(80), nullable=False)
    niveau = db.Column(db.String(80), nullable=False)

class Education(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    periode = db.Column(db.String(80), nullable=False)
    etablissement = db.Column(db.String(120), nullable=False)
    niveau = db.Column(db.String(80), nullable=False)
    diplome = db.Column(db.String(80), nullable=True) 

class Stage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    annee = db.Column(db.String(80), nullable=False)
    centre = db.Column(db.String(120), nullable=False)
    cadre = db.Column(db.String(120), nullable=False)
    diplome = db.Column(db.String(120), nullable=True)

# ----------------------------------------------------
# ROUTE PRINCIPALE
# ----------------------------------------------------

@app.route('/')
def home():
    # TRI CHRONOLOGIQUE pour les études universitaires (Licence -> M1 -> M2)
    experiences = Experience.query.order_by(asc(Experience.periode)).all()
    
    # TRI CHRONOLOGIQUE pour les études primaires/secondaires (CI -> Terminale)
    educations = Education.query.order_by(asc(Education.periode)).all()

    # TRI ANTÉCHRONOLOGIQUE pour les stages (le plus récent en premier)
    stages = Stage.query.order_by(desc(Stage.annee)).all()
    
    # Compétences (sans tri)
    competences = Competence.query.all()
    
    return render_template(
        'index.html', 
        experiences=experiences, 
        competences=competences, 
        educations=educations,
        stages=stages
    )

# ----------------------------------------------------
# DÉMARRAGE DU SERVEUR
# ----------------------------------------------------

if __name__ == '__main__':
    app.run(debug=True)