from socket import *


def server_start(host, port):
    sock = socket()
    sock.bind((host, port))
    sock.listen(1)
    conn, addr = sock.accept()
    while True:
    	data = conn.recv(1024)
    	
