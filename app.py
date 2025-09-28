from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy 
from sqlalchemy.orm import Session 

# CRUCIAL : Définissez explicitement le dossier static
app = Flask(__name__, static_folder='static') 

# --- Configuration de la Base de Données ---
# REMPLACEZ 'sqlite:///site.db' par votre URL de base de données Render pour le déploiement final !
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
db = SQLAlchemy(app) 
# ---------------------------------------------


# --- DÉFINITION DES MODÈLES DE BASE DE DONNÉES (POUR LA REQUÊTE) ---

class Experience(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    poste = db.Column(db.String(100), nullable=False)
    entreprise = db.Column(db.String(100), nullable=False)
    periode = db.Column(db.String(50), nullable=False)
    description = db.Column(db.Text)

class Competence(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(100), nullable=False)
    niveau = db.Column(db.String(50), nullable=False)

class Education(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    etablissement = db.Column(db.String(100), nullable=False)
    niveau = db.Column(db.String(50), nullable=False)
    periode = db.Column(db.String(50), nullable=False)
    diplome = db.Column(db.String(100))

class Stage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cadre = db.Column(db.String(100), nullable=False)
    centre = db.Column(db.String(100), nullable=False)
    annee = db.Column(db.String(20), nullable=False)
    diplome = db.Column(db.String(100))

# --- FIN DES MODÈLES ---


@app.route('/')
def index():
    # RÉCUPÉRATION DES DONNÉES DE LA BDD
    with Session(db.engine) as session:
        experiences_db = session.scalars(db.select(Experience)).all()
        educations_db = session.scalars(db.select(Education)).all()
        stages_db = session.scalars(db.select(Stage)).all()
        competences_db = session.scalars(db.select(Competence)).all()
        
    return render_template(
        'index.html',
        experiences=experiences_db,
        educations=educations_db,
        stages=stages_db,
        competences=competences_db
    )

if __name__ == '__main__':
    # Ceci est utile pour la création locale de la base de données au besoin
    # with app.app_context():
    #     db.create_all()
    app.run(debug=True)