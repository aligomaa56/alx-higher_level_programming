#!/usr/bin/python3
"""all states from hbtn_0e_0_usa database"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    mydb = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                           password=argv[2], database=argv[3])
    c = mydb.cursor()
    c.execute("SELECT * FROM states ORDER BY id ASC")
    for db in c:
        print(db)
    c.close()
    mydb.close()
