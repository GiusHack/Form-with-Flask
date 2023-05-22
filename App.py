from flask import Flask, render_template, request, redirect , url_for
import bleach.sanitizer
import re


app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/formulaire")
def formulaire():
    return render_template("formulaire.html")


@app.route("/traitement", methods=["POST", "GET"])
def traitement():
    if request.method == "POST":
        donnees = request.form
        nom = bleach.clean(donnees.get('nom'))
        prenom = bleach.clean(donnees.get('prénom'))
        email = bleach.clean(donnees.get('email'))
        genre = donnees.get('choix-genre')
        pays = donnees.get('pays')
        service = donnees.get('choix-service')
        commentaire = bleach.clean(donnees.get('commentaire'))
        donnees_completes = {}
        if nom and prenom and email and genre and pays and service and commentaire:
            donnees_completes = {
                'nom' : nom,
                'prenom': prenom,
                'email': email,
                'genre': genre,
                'pays': pays,
                'service': service
            }
            return render_template('traitement.html', donnees_completes=donnees_completes, commentaire=commentaire)
        else: 
            return render_template('traitement.html')
    else:
        return redirect(url_for('index'))
    
       
if __name__ == '__main__':
    app.run(debug=True)