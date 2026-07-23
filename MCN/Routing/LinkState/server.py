import socket

server = socket.socket()
server.bind(("localhost", 5000))
server.listen(1)

print("Server waiting...")

conn, addr = server.accept()
print("Connected to", addr)

lines = conn.recv(4096).decode().splitlines()

n = int(lines[0])

cost = []
for i in range(1, n + 1):
    cost.append(list(map(int, lines[i].split())))

src = int(lines[n + 1])

dist = cost[src][:]
visited = [False] * n
visited[src] = True

for _ in range(n - 1):
    u = min((i for i in range(n) if not visited[i]), key=lambda i: dist[i])
    visited[u] = True

    for v in range(n):
        if not visited[v] and cost[u][v] != 9999:
            dist[v] = min(dist[v], dist[u] + cost[u][v])

result = f"Shortest distances from node {src}: {dist}"

conn.send(result.encode())

conn.close()
server.close()