import pyshark
import socket
import time
#packet capture on tcp: port http
#locate the src, dst of the packet, analyze per second
#blacklist the ip permanently/temporarily based on how many connections they send to the server/sec

host, port = '192.168.0.101', 10000
detect=[]
connections=[]
blacklist = {
    'permanently': [],
    'temporarily': []
}

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

def handle():
    finish = time.time() + 3
    finishEND = time.time() + 60 * 15
    try:
        while time.time() < finish:
            conn, addr = server.accept()
            connections.append(addr[0])
    finally:
        for conn in connections:
            if connections.count(conn) > 1000:
                detect.append(conn)
                print(detect)
            if detect.count(conn) >= 10:
                blacklist['permanently'].append(conn)
                print(blacklist)
                break
            else:
                if not time.time() < finishEND:
                    detect.pop(0)
        connections.clear()

while True:
    handle()
