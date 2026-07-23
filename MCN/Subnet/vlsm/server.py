import socket
import math

def ip_to_int(ip):
    a, b, c, d = map(int, ip.split("."))
    return (a << 24) | (b << 16) | (c << 8) | d

def int_to_ip(n):
    return f"{(n>>24)&255}.{(n>>16)&255}.{(n>>8)&255}.{n&255}"

server = socket.socket()
server.bind(("localhost", 5000))
server.listen(1)

print("Server Waiting...")

conn, addr = server.accept()

data = conn.recv(4096).decode().splitlines()

base_ip = data[0]
n = int(data[1])
hosts = list(map(int, data[2:]))

hosts.sort(reverse=True)

current = ip_to_int(base_ip)

result = ""

for h in hosts:
    size = 2 ** math.ceil(math.log2(h + 2))
    cidr = 32 - int(math.log2(size))

    network = current
    broadcast = current + size - 1
    mask = (0xFFFFFFFF << (32 - cidr)) & 0xFFFFFFFF

    result += f"Hosts: {h}\n"
    result += f"Network: {int_to_ip(network)}/{cidr}\n"
    result += f"Mask: {int_to_ip(mask)}\n"
    result += f"First IP: {int_to_ip(network + 1)}\n"
    result += f"Last IP: {int_to_ip(broadcast - 1)}\n"
    result += f"Broadcast: {int_to_ip(broadcast)}\n\n"

    current += size

conn.send(result.encode())

conn.close()
server.close()