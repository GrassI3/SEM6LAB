import socket

client = socket.socket()
client.connect(("localhost", 5000))

ip = input("Enter IP Address: ")
cidr = input("Enter CIDR: ")
subnets = input("Enter number of subnets: ")

client.send(f"{ip} {cidr} {subnets}".encode())

result = client.recv(4096).decode()

print("\nResult:\n")
print(result)

client.close()