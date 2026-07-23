import socket

s = socket.socket()
s.connect(('localhost', 8080))
print("Connected to server!\n")

while True:
    msg = input("Client: ")
    s.send(msg.encode())
    print("Server:", s.recv(1024).decode())