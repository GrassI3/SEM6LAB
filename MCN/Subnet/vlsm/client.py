import socket

client = socket.socket()
client.connect(("localhost", 5000))

base_ip = input("Enter Base IP (e.g., 192.168.0.0): ")
n = int(input("Enter number of subnets: "))

msg = base_ip + "\n"
msg += str(n) + "\n"

for i in range(n):
    msg += input(f"Hosts for subnet {i+1}: ") + "\n"

client.send(msg.encode())

result = client.recv(4096).decode()

print("\nResult:\n")
print(result)

client.close()