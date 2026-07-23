import socket

client = socket.socket()
client.connect(("localhost", 5000))

data = input("Enter binary string: ")

client.send(data.encode())

result = client.recv(1024).decode()

print("\nNRZ-I Encoding:\n")
print(result)

client.close()