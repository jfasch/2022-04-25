import socket

conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conn.connect(('localhost', 1234))

while True:
    input('hallo, ist eine palette durchgefahren, dann drueckstu return')
    conn.send(b'abcd')
