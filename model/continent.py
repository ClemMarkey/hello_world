from model.db import Connect


class ContinentModel:
    def __init__(self):
        # appelle de la méthode static log() permettant de communiquer avec la base de données
        self.conn = Connect.log()

    def fetch_all(self):
        # requête permettant l'affichage de tous les continents
        self.conn.execute(
            """ SELECT id_continent, nom_continent from continent """)
        rows = self.conn.fetchall()
        return rows

    def deleteById(self, id):
        # requête permettant la suppression d'un continent
        self.conn.execute(
            f""" DELETE FROM continent WHERE id_continent = {id} """
        )

    def addContinent(self, continent):
        # requête permettant l'ajout d'un continent
        self.conn.execute(
            f"""INSERT INTO continent(id_continent, nom_continent) VALUES('{int(continent.get('id_continent'))}', '{continent.get('nom_continent')}')"""
        )

    def update(self, data):
        # méthode permettant la mise à jour d'un continent
        self.conn.execute(
            f""" UPDATE continent SET nom_continent = '{data.get('nom')}' WHERE id_continent = '{int(data.get('id'))}' """
        )
