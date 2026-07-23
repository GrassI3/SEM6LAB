import socket

server = socket.socket()
server.bind(("localhost", 5000))
server.listen(1)

print("Server waiting...")

conn, addr = server.accept()
print("Connected to", addr)

data = conn.recv(1024).decode().split()

d = list(map(int, data[:4]))
parity = data[4].lower()

p1 = d[0] ^ d[1] ^ d[3]
p2 = d[0] ^ d[2] ^ d[3]
p4 = d[1] ^ d[2] ^ d[3]

if parity == "odd":
    p1 ^= 1
    p2 ^= 1
    p4 ^= 1

result = f"Final Transmitted Sequence: {p1} {p2} {d[0]} {p4} {d[1]} {d[2]} {d[3]}"

conn.send(result.encode())

conn.close()
server.close()