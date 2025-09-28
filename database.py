import sqlite3
import os
# L'objet 'db' et les modèles sont maintenant importés LOCALEMENT dans la fonction.

def create_database():
    # Importation locale des modèles et de l'objet 'app'
    # Ceci est maintenant correct pour être appelé par 'python database.py' dans render.yaml
    from app import Experience, Competence, Education, Stage, app, db
    
    with app.app_context():
        # Crée toutes les tables définies
        db.create_all()

        if not Experience.query.first():
            
            # ----------------------------------------------------
            # I. ÉTUDES UNIVERSITAIRES (Ordre Chronologique : Licence -> M1 -> M2)
            # ----------------------------------------------------
            
            # 1. Licence (La plus ancienne)
            exp1 = Experience(
                poste='Licence Professionnelle en Génie Rural, Mécanisation Agricole, Pêche et Aquaculture',
                entreprise='Université d’Abomey Calavi / FSA',
                periode='2020 - 2024 (L1-L3)',
                description='Formation solide en ingénierie rurale. Soutenance de licence basée sur l\'étude et le **test d\'aliment pour poissons** (Aquaculture).'
            )
            
            # 2. Master 1
            exp2 = Experience(
                poste='Master 1 - Génie Rural et Mécanisation Agricole',
                entreprise='Université d’Abomey Calavi / FSA',
                periode='2024 - 2025 (M1)',
                description='Validation de la première année du cycle Master. Approfondissement des connaissances techniques et de recherche.'
            )
            
            # 3. Master 2 (La plus récente)
            exp3 = Experience(
                poste='Master 2 - Génie Rural et Mécanisation Agricole',
                entreprise='Université d’Abomey Calavi / FSA',
                periode='2025 - Aujourd\'hui (M2)',
                description='Poursuite et spécialisation en génie rural. Travaux avancés en gestion des équipements agricoles et développement durable.'
            )

            # ----------------------------------------------------
            # II. ÉTUDES PRIMAIRES ET SECONDAIRES (Reste inchangé)
            # ----------------------------------------------------

            edu1 = Education(periode='2007', etablissement='Ecole centre d’azowlissè', niveau='CI', diplome='')
            edu2 = Education(periode='2008-2009', etablissement='Ecole catholique sainte thérese de l’enfant jésus d’azowlissè', niveau='CP-CE1', diplome='')
            edu3 = Education(periode='2010-2013', etablissement='Ecole primaire public de Kpodédji', niveau='CE2-CM2', diplome='CEP')
            edu4 = Education(periode='2014', etablissement='CEG Azowlissè', niveau='6ème', diplome='')
            edu5 = Education(periode='2015-2016', etablissement='Complexe scolaire Jesus La Source', niveau='5ème-3ème', diplome='BEPC')
            edu6 = Education(periode='2017', etablissement='CEG Azowlissè', niveau='2nd', diplome='')
            edu7 = Education(periode='2018-2019', etablissement='Complexe scolaire la Grande Académie', niveau='1ère- Terminale', diplome='BAC D')

            # ----------------------------------------------------
            # III. STAGES & FORMATIONS PROFESSIONNELLES (Reste inchangé)
            # ----------------------------------------------------

            stage1 = Stage(annee='2024', centre='Ferme ALIK FISH FARM de Pobè', cadre='Stage Académique', diplome='')
            stage2 = Stage(annee='2023', centre='Ferme les anges de Dieu de Côme', cadre='Stage Académique', diplome='')
            stage3 = Stage(annee='2021', centre='CeFap Bénin', cadre='Formation professionnelle', diplome='Certificat de producteur d’éliciteur')
            
            # ----------------------------------------------------
            # IV. COMPÉTENCES CLÉS (Reste inchangé)
            # ----------------------------------------------------

            comp1 = Competence(nom='Pêche et Aquaculture', niveau='Expert') 
            comp2 = Competence(nom='Mécanisation Agricole', niveau='Expert')
            comp3 = Competence(nom='Ingénierie Rurale / Hydrologie', niveau='Avancé')
            comp4 = Competence(nom='Python/Flask (Développement Web)', niveau='Intermédiaire')
            comp5 = Competence(nom='SQL (Base de Données)', niveau='Intermédiaire')

            # ----------------------------------------------------
            # AJOUT DANS LA BASE DE DONNÉES
            # ----------------------------------------------------
            
            db.session.add(exp1)
            db.session.add(exp2)
            db.session.add(exp3)
            
            db.session.add(edu1)
            db.session.add(edu2)
            db.session.add(edu3)
            db.session.add(edu4)
            db.session.add(edu5)
            db.session.add(edu6)
            db.session.add(edu7)
            
            db.session.add(stage1)
            db.session.add(stage2)
            db.session.add(stage3)

            db.session.add(comp1)
            db.session.add(comp2)
            db.session.add(comp3)
            db.session.add(comp4)
            db.session.add(comp5)
            
            db.session.commit()
            print("Base de données créée et remplie !")
        else:
            print("La base de données contenait déjà des données.")

if __name__ == '__main__':
    from app import app, db # Importation des objets nécessaires pour l'exécution locale
    create_database()