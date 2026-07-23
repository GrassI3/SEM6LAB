import socket
import random

server = socket.socket()
server.bind(("localhost", 5000))
server.listen(1)

print("Server waiting...")

conn, addr = server.accept()
print("Connected to", addr)

frames = int(conn.recv(1024).decode())

i = 1
result = ""

while i <= frames:
    result += f"Sending Frame {i}...\n"

    if random.random() > 0.25:
        result += f"ACK received for Frame {i}.\n\n"
        i += 1
    else:
        result += f"ACK lost. Retransmitting Frame {i}...\n\n"

conn.send(result.encode())

conn.close()
server.close()