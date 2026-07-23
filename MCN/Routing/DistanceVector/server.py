import socket

server = socket.socket()
server.bind(("localhost", 5000))
server.listen(1)

print("Server waiting...")

conn, addr = server.accept()
print("Connected to", addr)

lines = conn.recv(4096).decode().splitlines()

V, E = map(int, lines[0].split())

edges = []
for i in range(1, E + 1):
    edges.append(list(map(int, lines[i].split())))

src = int(lines[E + 1])

dist = [9999] * V
dist[src] = 0

for _ in range(V - 1):
    for u, v, w in edges:
        if dist[u] != 9999 and dist[u] + w < dist[v]:
            dist[v] = dist[u] + w

result = f"Distance Vector from node {src}: {dist}"

conn.send(result.encode())

conn.close()
server.close()