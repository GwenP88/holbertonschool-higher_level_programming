#!/usr/bin/python3
"""Connects to a MySQL database
and lists all cities of a given state."""
import sys
import MySQLdb

if __name__ == "__main__":

    user = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=user,
        passwd=password,
        db=database,
        charset="utf8"
    )

    cur = conn.cursor()
    cur.execute(
        "SELECT cities.name FROM cities "
        "JOIN states ON cities.state_id = states.id "
        "WHERE states.name = %s "
        "ORDER BY cities.id ASC", (state_name,)
    )
    query_rows = cur.fetchall()
    list_cities = []
    for row in query_rows:
        list_cities.append(row[0])
    print(", ".join(list_cities))
    cur.close()
    conn.close()
