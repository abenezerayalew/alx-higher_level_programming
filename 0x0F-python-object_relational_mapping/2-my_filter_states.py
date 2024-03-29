#!/usr/bin/python3
""" Select states whhere names matching arguments """
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
    cur.execute(("SELECT id, name FROM states WHERE states.name = \'{}\' \
                  ORDER BY states.id ASC ").format(stateName))
    for row in cur.fetchall():
        print(row)
