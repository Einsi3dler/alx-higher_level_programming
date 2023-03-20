#!/usr/bin/python3
"""
a script that lists all cities from the database hbtn_0e_4_usa extracts result by state
"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=argv[1], passwd=argv[2], db=argv[3])
    cursor = db.cursor()
    stateName = argv[4]
    params = (stateName,)
    query = "SELECT cities.id, cities.name, states.name FROM cities, states WHERE cities.state_id = states.id AND states.name=%s ORDER BY cities.id ASC"
    cursor.execute(query, params)
    query_rows = cursor.fetchall()
    x=0
    for row in query_rows:
        if x==len(query_rows) - 1:
            print(row[1])
            break
        print(row[1],end=", ")
        x = x+1
    cursor.close()
    db.close()
