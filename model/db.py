from abc import ABC
import mysql.connector


class Connect(ABC):

    conn = mysql.connector.connect(
        # informations de connection avec la bdd pour se connecter
        host="db",
        user="root",
        password="root",
        database="beer",
        port="3306"
    )
    # commit automatique quand un requête est faite en bdd
    conn.autocommit = True

    @staticmethod
    def log():
        try:
            # connection à la base de données
            cursor = Connect.conn.cursor()
            return cursor
        except mysql.connector.Error as err:
            # message d'erreur si une erreur se produit
            print(err)
