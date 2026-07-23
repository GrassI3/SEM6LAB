import socket
import math

def ip_to_int(ip):
    octets = list(map(int, ip.split(".")))
    return sum(octets[i] << (24 - 8 * i) for i in range(4))

def int_to_ip(value):
    return ".".join(str((value >> shift) & 255) for shift in (24, 16, 8, 0))

def mask_from_cidr(cidr):
    mask_bits = "1" * cidr + "0" * (32 - cidr)
    return [int(mask_bits[i:i+8], 2) for i in range(0, 32, 8)]

server = socket.socket()
server.bind(("localhost", 5000))
server.listen(1)

print("Server waiting...")

conn, addr = server.accept()
print("Connected to", addr)

ip_input, cidr, subnet_count = conn.recv(1024).decode().split()

cidr = int(cidr)
subnet_count = int(subnet_count)

subnet_bits = math.ceil(math.log2(subnet_count))
new_cidr = cidr + subnet_bits

base_mask = mask_from_cidr(cidr)

octets = list(map(int, ip_input.split(".")))
network_octets = [octets[i] & base_mask[i] for i in range(4)]
network_int = ip_to_int(".".join(map(str, network_octets)))

block_size = 1 << (32 - new_cidr)
total_subnets = 1 << subnet_bits

result = ""
result += "New Mask: " + ".".join(map(str, mask_from_cidr(new_cidr))) + "\n"
result += f"Number of subnets created: {total_subnets}\n\n"

for i in range(total_subnets):
    subnet_network = network_int + i * block_size
    subnet_broadcast = subnet_network + block_size - 1

    result += f"Subnet {i+1}:\n"
    result += f"Network:   {int_to_ip(subnet_network)}\n"
    result += f"Broadcast: {int_to_ip(subnet_broadcast)}\n\n"

conn.send(result.encode())

conn.close()
server.close()