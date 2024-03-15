#!/usr/bin/python3
"""script that lists all states from the database hbtn_0e_0_usa"""
import MySQLdb
from sys import argv

mydb = MySQLdb.connect(
    host="localhost",
    port=3306,
    user=argv[1],
    passwd=argv[2],
    database=argv[3],
)
c = mydb.cursor()
c.execute("SELECT * FROM states ORDER BY id ASC")
rows = cur.fetchall()
for db in rows:
    print(row)
c.close()
mydb.close()
