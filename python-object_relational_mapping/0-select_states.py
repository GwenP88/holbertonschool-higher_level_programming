#!/usr/bin/python3
"""Connects to a MySQL database and lists all states ordered by id."""
import sys
import MySQLdb

if __name__ == "__main__":

    user = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # connection à MySQL - garder la connection dans une variable
    conn = MySQLdb.connect(
        host="localhost",
        port=3306, user=user,
        passwd=password,
        db=database,
        charset="utf8"
        )

    # creation du curseur à partir de la connection
    # cursor = outil pour envoyer des requêtes
    cur = conn.cursor()

    # exécuter la requête voulue par le curseur.
    cur.execute("SELECT * FROM states ORDER BY id ASC")

    # récupérer toutes les lignes obtenu via la requête
    query_rows = cur.fetchall()

    # parcourir toutes ces lignes
    for row in query_rows:
        # afficher toutes les lignes
        print(row)

    # fermer le cursor
    cur.close()

    # fermer la connection
    conn.close()
