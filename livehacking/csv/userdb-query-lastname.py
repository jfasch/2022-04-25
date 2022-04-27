import sys
import sqlite3


sqlitefilename = sys.argv[1]
lastname = sys.argv[2]

connection = sqlite3.connect(sqlitefilename)
cursor = connection.cursor()

stmt = f'select * from userdb where lastname = ?;'

resultset = cursor.execute(stmt, (lastname,))

for id, firstname, lastname, birth in resultset:
    print(id, firstname, lastname, birth)

connection.commit()
