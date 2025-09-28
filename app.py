from flask import Flask, render_template
# NOUVEAU : Importez Flask-SQLAlchemy pour définir l'objet 'db'
from flask_sqlalchemy import SQLAlchemy 

# CRUCIAL : assurez-vous que static_folder est bien 'static'
# Nous pouvons aussi le définir explicitement pour Render
app = Flask(__name__, static_folder='static') 

# --- Configuration de la Base de Données (Ajoutée pour résoudre l'ImportError) ---
# Ceci est nécessaire car un autre fichier (probablement database.py) essaie d'importer 'db'.
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 

# Définition de l'objet 'db' que Render et vos autres fichiers essaient d'importer
db = SQLAlchemy(app) 
# --------------------------------------------------------------------------------


# --- Vos données (assurez-vous que ces listes sont bien définies) ---
experiences = [
    # Exemple de données (remplacez par les vôtres)
    {'poste': 'Étudiant en Licence 1', 'entreprise': 'Ecole Polytechnique d\'Abomey-Calavi (EPAC)', 'periode': '2023 - Aujourd\'hui', 'description': "Formation d'Ingénieur en Génie Electrique et Informatique Industrielle (GEII)."},
]
educations = [
    {'etablissement': 'Lycée Technique d\'Azowlisse', 'niveau': 'Secondaire', 'periode': '2019-2023', 'diplome': 'Baccalauréat Série C'},
]
stages = [
    {'cadre': 'Stage d\'initiation', 'centre': 'Entreprise locale de maintenance', 'annee': '2024'},
]
competences = [
    {'nom': 'Python', 'niveau': 'Débutant/Intermédiaire'},
    {'nom': 'HTML & CSS', 'niveau': 'Intermédiaire'},
]
# -------------------------------------------------------------------


@app.route('/')
def index():
    return render_template(
        'index.html',
        experiences=experiences,
        educations=educations,
        stages=stages,
        competences=competences
    )

if __name__ == '__main__':
    # Vous pouvez ajouter cette ligne pour créer la base de données locale si nécessaire
    # with app.app_context():
    #     db.create_all()
    
    # Lancez l'application en mode debug
    app.run(debug=True)