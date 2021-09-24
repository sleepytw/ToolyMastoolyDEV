import threading
import socket

host='localhost'
port=23

sock = socket.socket()
sock.connect((host, port))

def handle(message):
    threading.Timer(5, handle).start()
    sock.send(message)

handle(b'Alive')
