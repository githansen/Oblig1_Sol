import socket
import select
import time

host = socket.gethostbyname(socket.gethostname())  # Host IP
port = 80
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Create socket and bind
sock.bind((host, port))

sock.listen()
while True:
    #Establish the connection
    print ('\n\nReady to serve...')
    c, addr = sock.accept()
    msg = c.recv(1024).decode()
    print(msg)
    filename= msg.split()[1]
    f = open(filename[1:])
    output = f.read()
    c.send("HTTP/1.1 200 OK\r\n\r\n".encode())
    c.send(output.encode())
