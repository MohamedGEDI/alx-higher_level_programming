#!/usr/bin/python3
import MySQLdb
import sys
if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    host = 'localhost'
    port = 3306
    conn = MySQLdb.connect(host=host, user=username, passwd=password,
                           db=db_name, port=port)
    cur = conn.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    query_row = cur.fetchall()
    i = 0
    for state in query_row:
        print(state)
    cur.close()
    conn.close()
