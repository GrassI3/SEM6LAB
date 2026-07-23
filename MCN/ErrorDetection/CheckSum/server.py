import socket

server = socket.socket()
server.bind(("localhost", 5000))
server.listen(1)

print("Server waiting...")

conn, addr = server.accept()
print("Connected to", addr)

data = list(map(int, conn.recv(1024).decode().split()))

s = sum(data)
checksum = ~s & 0xFF

result = f"Sum: {s}\n"
result += f"Generated Checksum: {checksum}"

conn.send(result.encode())

conn.close()
server.close()