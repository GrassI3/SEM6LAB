import socket

server = socket.socket()
server.bind(("localhost", 5000))
server.listen(1)

print("Server waiting...")

conn, addr = server.accept()
print("Connected to", addr)

data = conn.recv(1024).decode()

stuffed = data.replace("E", "EE").replace("F", "EF")

result = f"Framed Data: F{stuffed}F"

conn.send(result.encode())

conn.close()
server.close()