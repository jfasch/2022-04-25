import sys
import userdb_csv


users = userdb_csv.read_csv_header(sys.argv[1])
for u in users:
    print(f'ID:{u["id"]}, Firstname:{u["firstname"]}, Lastname:{u["lastname"]}, Date of birth: {u["birth"]}')
