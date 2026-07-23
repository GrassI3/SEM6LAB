import socket

server = socket.socket()
server.bind(("localhost", 5000))
server.listen(1)

print("Server waiting...")

conn, addr = server.accept()
print("Connected to", addr)

data, gen = conn.recv(1024).decode().split()

div = list(data + '0' * (len(gen) - 1))

for i in range(len(data)):
    if div[i] == '1':
        for j in range(len(gen)):
            div[i + j] = str(int(div[i + j]) ^ int(gen[j]))

crc = "".join(div)[-(len(gen) - 1):]

result = f"Generated CRC: {crc}\n"
result += f"Transmitted Data: {data + crc}"

conn.send(result.encode())

conn.close()
server.close()