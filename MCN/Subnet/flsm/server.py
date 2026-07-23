import socket
import math

server = socket.socket()
server.bind(("localhost", 5000))
server.listen(1)

print("Server Waiting...")

conn, addr = server.accept()

ip, cidr, subnets = conn.recv(1024).decode().split()

cidr = int(cidr)
subnets = int(subnets)

subnet_bits = math.ceil(math.log2(subnets))
new_cidr = cidr + subnet_bits
block = 2 ** (32 - new_cidr)

parts = ip.split(".")
base = ".".join(parts[:3])
start = int(parts[3]) // (2 ** (32 - cidr)) * (2 ** (32 - cidr))

result = f"New CIDR: /{new_cidr}\n"
result += f"Block Size: {block}\n\n"

for i in range(subnets):
    network = start + i * block
    broadcast = network + block - 1

    result += f"Subnet {i+1}\n"
    result += f"Network: {base}.{network}\n"
    result += f"Broadcast: {base}.{broadcast}\n\n"

conn.send(result.encode())
conn.close()
server.close()