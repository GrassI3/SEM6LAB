import socket

server = socket.socket()
server.bind(("localhost", 5000))
server.listen(1)

print("Server waiting...")

conn, addr = server.accept()
print("Connected to", addr)

data = conn.recv(1024).decode()

stuffed = data.replace("11111", "111110")

result = f"Framed Data: 01111110 {stuffed} 01111110"

conn.send(result.encode())

conn.close()
server.close()