# FLASK les bases

## **Getting Started**

---

### **Import de la classe Flask**

`from flask import Flask`

---

### **Instanciation de la classe**

`app = Flask(__name__)`

`__name__` fait référence au nom du module ou du package actuel

---

### **Ajout de routes**

`@app.route('/')` est un décorateur permettant de définir à Flask quelle URL doit déclencher une fonction

`def hello():` est la fonction associée à l'URL

---

### **Route avec paramètres**

`@app.route('/delete/<int:id>')`

le type n'est pas obligatoire

---

### **Récupération des données reçus depuis un formulaire**

```
@app.route('/validate/', methods=['POST', 'GET'])
request.form['nom_paramètre']
```

### **Lancer l'application**

`flask run`

ou permettre la mise à jour en temps réelle

`flask run --reload`

### **Mise en place des variables sessions**

on commence par importer les sessions depuis flask

on définit une clé secrète pour nos sessions

on crée nos variables

comme les variables sont créées dans app.py, elles sont propagées dans toute l'application

```
from flask import session
app = Flask(__name__)
app.secret_key = "nom de la clé secrète"

session['nom_de_la_variable'] = "value"
```

### **Suppression d'une variable session**

```
session.pop('nom_de_la_variable', default=None)
```
