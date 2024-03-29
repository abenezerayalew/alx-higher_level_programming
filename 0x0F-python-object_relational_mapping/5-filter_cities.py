#!/usr/bin/python3
""" Select states with names matching arguments """


from sys import argv
import MySQLdb

if __name__ == '__main__':

    db_user = argv[1]
    db_passwd = argv[2]
    db_name = argv[3]
    search_state = '{}'.format(argv[4])

    database = MySQLdb.connect(host='localhost',
                               port=3306,
                               user=db_user,
                               passwd=db_passwd,
                               db=db_name)

    cursor = database.cursor()
    cursor.execute('SELECT cities.name FROM cities\
                   JOIN states\
                   ON cities.state_id = states.id\
                   WHERE states.name = %s\
                   ORDER BY states.id ASC', (search_state,))
    for row in cursor.fetchall():
        print(row)
