import socket
import random

server = socket.socket()
server.bind(("localhost", 5000))
server.listen(1)

print("Server waiting...")

conn, addr = server.accept()
print("Connected to", addr)

data = conn.recv(1024).decode().split()
frames = int(data[0])
window = int(data[1])

acked = [False] * (frames + 1)
i = 1
result = ""

while i <= frames:
    current_window = range(i, min(i + window, frames + 1))

    for j in current_window:
        if not acked[j]:
            result += f"Sending Frame {j}\n"

    for j in current_window:
        if not acked[j]:
            if random.random() > 0.2:
                result += f"ACK received for {j}\n"
                acked[j] = True
            else:
                result += f"ACK lost for {j}. Will repeat.\n"

    while i <= frames and acked[i]:
        i += 1

    result += "-" * 20 + "\n"

conn.send(result.encode())

conn.close()
server.close()