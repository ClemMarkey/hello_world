from flask import render_template


class ContinentController():

    def fetch_continent(self, model):
        # affichage de la page d'accueil avec les données provenants de la méthode fetch_all du model
        return render_template('select.html', obj=model.fetch_all())

    def vue_add_continent(self):
        # affichage du formulaire d'ajout de continent
        return render_template('formulaire.html')

    def delete_by_id(self, model, id):
        # appelle de la méthode du modèle permettant la suppression d'un continent, on lui passe en paramètre l'id du continent
        return model.deleteById(id)

    def add(self, model,  continent):
        # appelle de la méthode du modèle permettant l'ajout d'un continent en base de données, on lui envoie les paramètres
        return model.addContinent(continent)

    def vue_update_continent(self, data):
        # affichage du formulaire d'update d'un continent, on lui donne la data du continent à modifier
        return render_template('formulaire_update.html', data=data)

    def update(self, model, data):
        # appelle de la méthode du modèle permettant la mise à jour en bdd d'un continent
        return model.update(data)
