from flask.scaffold import F
from werkzeug.utils import redirect
from controller.continent import ContinentController
from model.continent import ContinentModel
from flask import Flask, request, url_for

app = Flask(__name__)

contModel = ContinentModel()
contController = ContinentController()


@app.route('/')
# route de base de l'application
def select():
    return contController.fetch_continent(contModel)


@app.route('/delete/<int:id>')
# route permettant la suppression d'un continent, on récupère l'id dans l'url
def suppr(id):
    # on appelle le controller, la méthode permettant la suppression et on lui passe en paramètre le model et le paramètre id
    contController.delete_by_id(contModel, id)
    # on redirige vers la page d'accueil
    return redirect(url_for("select"))


@app.route('/formulaire/')
# route permettant de se rendre sur le formulaire d'ajout de continent
def formulaire_add_continent():
    # on appelle la vue permettant d'afficher le formulaire d'ajout de continent
    return contController.vue_add_continent()


@app.route('/addContinent/', methods=['POST', 'GET'])
# route permettant d'ajouter un continent en base de données, on utilise la méthode post dans le formulaire
def add_continent():
    # on stock les données (ici de type multidict) dans formData
    formData = request.form
    # on envoie les données dans le controller avec le model
    contController.add(contModel, formData)
    # on redirige vers la page d'accueil
    return redirect(url_for("select"))


@app.route('/update_formulaire/')
# route permettant de se rendre sur le formulaire de mise à jour d'un continent, les données concernant le continent à mettre à jour sont dans l'url
def formulaire_update():
    # on récupère les données de l'url pour les stocker dans formData
    formData = request.args
    # on appelle le controller qui affichera la vue avec les données du continent à mettre à jour
    return contController.vue_update_continent(formData)


@app.route('/update_continent/', methods=['POST', 'GET'])
# route permettant de mettre à un jour un continent en base de données, on récupère les données en POST
def update_continent():
    # on stock les données dans formData
    formData = request.form
    # on appelle le controller permettant la mise à jour en base de données
    contController.update(contModel, formData)
    # on redirige vers la page d'accueil
    return redirect(url_for("select"))


app.run(debug=True, host='0.0.0.0')
