import socket

client = socket.socket()
client.connect(("localhost", 5000))

n = int(input("Enter number of nodes: "))

msg = str(n) + "\n"

print("Enter cost matrix (row by row, use 9999 for infinity):")
for _ in range(n):
    msg += input() + "\n"

src = input("Enter source node: ")
msg += src

client.send(msg.encode())

result = client.recv(1024).decode()

print("\nResult:\n")
print(result)

client.close()