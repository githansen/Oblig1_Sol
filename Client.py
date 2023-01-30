import socket 
import sys
host = socket.gethostbyname(socket.gethostname())  # Host IP
print(host)
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect((host, 80))
msg = "GET /" + "index.html" + " HTTP/1.1\r\n" + "Host: " + host + ":" + str(socket.getsockname()[1]) + "\r\n\r\n"
socket.send(msg.encode())

print ("\n\n---------------HTTP RESPONSE---------------\n")
response=socket.recv(1024).decode()
print(response)

fileData = socket.recv(10000).decode()
print(fileData)

