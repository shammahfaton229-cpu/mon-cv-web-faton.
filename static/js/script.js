document.addEventListener('DOMContentLoaded', function() {
    // Récupérer la modale
    var modal = document.getElementById("myModal");

    // Récupérer l'image et l'insérer dans la modale
    var img = document.getElementById("myImg"); // L'ID de votre image de profil
    var modalImg = document.getElementById("img01");

    // Quand on clique sur l'image de profil
    if (img) { // S'assurer que l'image existe
        img.onclick = function(){
            modal.style.display = "flex"; // Afficher la modale
            modalImg.src = this.src; // Mettre la source de l'image cliquée
        }
    }

    // Récupérer le bouton de fermeture (X)
    var span = document.getElementsByClassName("close")[0];

    // Quand on clique sur (X), fermer la modale
    if (span) { // S'assurer que le bouton de fermeture existe
        span.onclick = function() {
            modal.style.display = "none";
        }
    }

    // Fermer la modale si l'utilisateur clique en dehors de l'image
    window.onclick = function(event) {
        if (event.target == modal) {
            modal.style.display = "none";
        }
    }
});