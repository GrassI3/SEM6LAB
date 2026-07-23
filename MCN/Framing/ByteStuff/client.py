import socket

client = socket.socket()
client.connect(("localhost", 5000))

data = input("Enter data string: ")

client.send(data.encode())

result = client.recv(1024).decode()

print("\nResult:\n")
print(result)

client.close()