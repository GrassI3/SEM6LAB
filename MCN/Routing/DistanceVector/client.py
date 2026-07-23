import socket

client = socket.socket()
client.connect(("localhost", 5000))

V, E = map(int, input("Enter number of Vertices and Edges: ").split())

msg = f"{V} {E}\n"

print("Enter edges (source dest weight):")
for _ in range(E):
    msg += input() + "\n"

src = input("Enter source node: ")
msg += src

client.send(msg.encode())

result = client.recv(1024).decode()

print("\nResult:\n")
print(result)

client.close()