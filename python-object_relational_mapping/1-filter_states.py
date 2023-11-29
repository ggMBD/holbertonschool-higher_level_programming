#!/usr/bin/python3
"""
Script that lists all states with a name starting with N (upper N) from the database hbtn_0e_0_usa:
"""

import MySQLdb
import sys

if __name__ == "__main__":
    """
    Main function to connect to the MySQL server and fetch states data.
    """

    username, password, database = sys.argv[1:4]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )
    """Create a cursor object to interact with the database."""
    cursor = db.cursor()

    query = "SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id"
    cursor.execute(query)

    results = cursor.fetchall()
    for row in results:
        print(row)
