import userdb_csv

import sys
from pprint import pprint
import sqlite3


format = sys.argv[1]
csvfilename = sys.argv[2]
sqlitefilename = sys.argv[3]


if format == 'noheader':
    func = userdb_csv.read_csv_noheader
elif format == 'header':
    func = userdb_csv.read_csv_header
else:
    print('bad format:', format)
    sys.exit(1)

connection = sqlite3.connect(sqlitefilename)

cursor = connection.cursor()

for user in func(csvfilename):
    id = user['id']
    firstname = user['firstname']
    lastname = user['lastname']
    birth = user['birth']

    cursor.execute(f'insert into userdb values ({id}, "{firstname}", "{lastname}", "{birth}");')

connection.commit()
