import subprocess
import socket
import os

host = 'localhost'
port = 23

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

def receive():
    while True:
        client, addr = server.accept()
        message = client.recv(1024)
        if b'Alive' in message:
            print('%s is online!')

print('Server is listening for clients...')
receive()
