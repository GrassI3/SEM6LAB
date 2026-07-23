import socket

server = socket.socket()
server.bind(("localhost", 5000))
server.listen(1)

print("Server waiting...")

conn, addr = server.accept()
print("Connected to", addr)

data = conn.recv(1024).decode()

result = "Bit\tFirst Half\tSecond Half\n"

for b in data:
    if b == '0':
        result += f"{b}\t+1V\t-1V\n"
    else:
        result += f"{b}\t-1V\t+1V\n"

conn.send(result.encode())

conn.close()
server.close()