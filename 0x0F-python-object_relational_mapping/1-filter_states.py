#!/usr/bin/python3
# script that lists all states with a name starting with N (upper N) from the database
import sys
import MySQLdb
def starting_N():
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    conn = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=db_name, charset="utf8")
    cur = conn.cursor()
    # AND states.id>5
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%'" + "ORDER BY states.id ASC" )
    query_rows = cur.fetchall()
    if query_rows:
        for row in query_rows:
            print(row)
    cur.close()
    conn.close()
if __name__ == "__main__":
    starting_N()