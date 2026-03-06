#!/usr/bin/python3
"""Connects to a MySQL database
and takes in an argument
and displays all values in the states table
of hbtn_0e_0_usa where name matches the argument"""
import sys
import MySQLdb

if __name__ == "__main__":

    user = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    searched = sys.argv[4]

    conn = MySQLdb.connect(
        host="localhost",
        port=3306, user=user,
        passwd=password,
        db=database,
        charset="utf8"
        )

    cur = conn.cursor()
    cur.execute(
        "SELECT * FROM states "
        "WHERE BINARY name = '{}' "
        "ORDER BY id ASC".format(searched)
        )
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
