import socket

server = socket.socket()
server.bind(("localhost", 5000))
server.listen(1)

print("Server waiting...")

conn, addr = server.accept()
print("Connected to", addr)

data = conn.recv(1024).decode().split()

r = list(map(int, data[:7]))
mode = data[7].lower()

c1 = r[0] ^ r[2] ^ r[4] ^ r[6]
c2 = r[1] ^ r[2] ^ r[5] ^ r[6]
c4 = r[3] ^ r[4] ^ r[5] ^ r[6]

if mode == "odd":
    c1 ^= 1
    c2 ^= 1
    c4 ^= 1

error_pos = (c4 * 4) + (c2 * 2) + c1

result = ""

if error_pos == 0:
    result += "Status: No error detected in received data.\n"
else:
    result += f"Status: Error detected at position {error_pos}.\n"
    r[error_pos - 1] ^= 1
    result += f"Corrected Hamming Code: {' '.join(map(str, r))}\n"

result += f"Extracted Data Bits: {r[2]} {r[4]} {r[5]} {r[6]}"

conn.send(result.encode())

conn.close()
server.close()