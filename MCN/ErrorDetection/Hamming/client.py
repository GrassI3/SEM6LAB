import socket

client = socket.socket()
client.connect(("localhost", 5000))

bits = input("Enter 7 received bits (space separated): ")
mode = input("Enter parity mode (even/odd): ")

client.send(f"{bits} {mode}".encode())

result = client.recv(1024).decode()

print("\nResult:\n")
print(result)

client.close()