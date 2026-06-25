# program2 : Write a HTTP web client program to download a web page using TCP sockets

import socket

HOST = "example.com"
PORT = 80

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
s.send(b"GET / HTTP/1.1\r\nHost: example.com\r\nConnection: close\r\n\r\n")

while True:
    data = s.recv(1024)
    if not data:
        break
    print(data.decode(), end="")

s.close()