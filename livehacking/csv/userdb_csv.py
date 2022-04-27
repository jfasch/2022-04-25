import csv


def read_csv_noheader(filename):
    users = []
    f = open(filename, encoding='cp1252')
    rdr = csv.reader(f, delimiter=';', quotechar='"')
    for id, firstname, lastname, birth in rdr:
        users.append(
            {
                'id': id,
                'firstname': firstname,
                'lastname': lastname,
                'birth': birth,
            }
        )
    return users

def read_csv_header(filename):
    users = []
    f = open(filename, encoding='cp1252')
    rdr = csv.DictReader(f, delimiter=';', quotechar='"')
    for element in rdr:
        id = int(element['ID'])
        firstname = element['First name']
        lastname = element['Last name']
        birth = element['Date of Birth']

        users.append(
            {
                'id': id,
                'firstname': firstname,
                'lastname': lastname,
                'birth': birth,
            }
        )

    return users
