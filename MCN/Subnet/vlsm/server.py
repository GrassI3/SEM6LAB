import socket
import math

def ip_to_int(ip_str):
    octets = list(map(int, ip_str.split(".")))
    return (octets[0] << 24) + (octets[1] << 16) + (octets[2] << 8) + octets[3]

def int_to_ip(ip_int):
    return f"{(ip_int >> 24) & 255}.{(ip_int >> 16) & 255}.{(ip_int >> 8) & 255}.{ip_int & 255}"

server = socket.socket()
server.bind(("localhost", 5000))
server.listen(1)

print("Server waiting...")

conn, addr = server.accept()
print("Connected to", addr)

lines = conn.recv(4096).decode().splitlines()

base_ip = lines[0]
n = int(lines[1])
hosts = list(map(int, lines[2:]))

hosts.sort(reverse=True)

current_ip_int = ip_to_int(base_ip)

result = "--- Proper VLSM Allocation Table ---\n\n"

for req in hosts:
    size = 2 ** math.ceil(math.log2(req + 2))
    cidr = 32 - int(math.log2(size))

    mask = (0xFFFFFFFF << (32 - cidr)) & 0xFFFFFFFF
    broadcast = current_ip_int + size - 1

    result += f"Subnet (Req: {req} hosts)\n"
    result += f"Network:   {int_to_ip(current_ip_int)}/{cidr}\n"
    result += f"Mask:      {int_to_ip(mask)}\n"
    result += f"First IP:  {int_to_ip(current_ip_int + 1)}\n"
    result += f"Last IP:   {int_to_ip(broadcast - 1)}\n"
    result += f"Broadcast: {int_to_ip(broadcast)}\n\n"

    current_ip_int += size

conn.send(result.encode())

conn.close()
server.close()