#!/usr/bin/python3
# script that takes in an argument and displays all values
from sys import argv
import MySQLdb

if __name__ == '__main__':
    db_user = argv[1]
    db_passwd = argv[2]
    db_name = argv[3]
    stateName = argv[4]
    database = MySQLdb.connect(
                host='localhost',
                port=3306,
                user=db_user,
                passwd=db_passwd,
                db=db_name)
    cur = database.cursor()
    cur.execute(("SELECT * FROM states WHERE name = \'{}\' \
                  ORDER BY states.id ASC ").format(stateName))
    for row in cur.fetchall():
        print(row)
