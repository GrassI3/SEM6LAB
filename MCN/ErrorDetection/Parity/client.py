import socket

client = socket.socket()
client.connect(("localhost", 5000))

bits = input("Enter 4 data bits (space separated): ")
parity = input("Enter parity mode (even/odd): ")

client.send(f"{bits} {parity}".encode())

result = client.recv(1024).decode()

print("\nResult:\n")
print(result)

client.close()