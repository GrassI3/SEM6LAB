import socket

server = socket.socket()
server.bind(("localhost", 5000))
server.listen(1)

print("Server waiting...")

conn, addr = server.accept()
print("Connected to", addr)

data = conn.recv(1024).decode()

curr = 1
result = "Result:\n"

for b in data:
    if b == '1':
        curr = -curr
    voltage = "+1V" if curr == 1 else "-1V"
    result += f"{voltage}\t"

conn.send(result.encode())

conn.close()
server.close()