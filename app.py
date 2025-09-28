from flask import Flask, render_template

# CRUCIAL : assurez-vous que static_folder est bien 'static'
app = Flask(__name__) 

# --- Vos données (assurez-vous que ces listes sont bien définies) ---
# Si vous avez une base de données, adaptez cette partie.
# Ces listes doivent être définies quelque part avant d'être passées au template.

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
    # Lancez l'application en mode debug
    app.run(debug=True)