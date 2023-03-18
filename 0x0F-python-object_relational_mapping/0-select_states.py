#!/usr/bin/python3
import sys
import MySQLdb
#script that lists all states from the database hbtn_0e_0_usa
def list_all_state():
    '''list all states in DataBase'''
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    conn = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=db_name, charset="utf8")
    cur = conn.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC") 
    query_rows = cur.fetchall()
    if query_rows:
        for row in query_rows:
            print(row)
    cur.close()
    conn.close()
if __name__ == "__main__":
    list_all_state()
