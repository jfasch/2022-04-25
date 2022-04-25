import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 1234))
server_socket.listen()

while True:
    connection, client_addr = server_socket.accept()
    print('jetzt hamma eine connection, und zwar von', client_addr)
    while True:
        data = connection.recv(4)

        print(data)

