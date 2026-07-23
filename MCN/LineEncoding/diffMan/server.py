import socket

server = socket.socket()
server.bind(("localhost", 5000))
server.listen(1)

print("Server waiting...")

conn, addr = server.accept()
print("Connected to", addr)

data = conn.recv(1024).decode()

curr = 1
result = "Bit\tFirst Half\tSecond Half\n"

for b in data:
    if b == '0':
        curr = -curr          # Transition at beginning for 0

    first = "+1V" if curr == 1 else "-1V"

    curr = -curr              # Mandatory middle transition

    second = "+1V" if curr == 1 else "-1V"

    result += f"{b}\t{first}\t{second}\n"

conn.send(result.encode())

conn.close()
server.close()