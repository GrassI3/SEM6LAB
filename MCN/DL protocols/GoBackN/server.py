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

i = 1
result = ""

while i <= frames:
    current_window = list(range(i, min(i + window, frames + 1)))
    result += f"Sending window: {current_window}\n"

    lost_frame = 0

    for j in current_window:
        if random.random() < 0.2:
            result += f"ACK lost for {j}. Going back.\n"
            if lost_frame == 0:
                lost_frame = j
        else:
            result += f"ACK received for {j}\n"

    if lost_frame == 0:
        i += window
    else:
        i = lost_frame

    result += "-" * 20 + "\n"

conn.send(result.encode())

conn.close()
server.close()