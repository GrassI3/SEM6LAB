import socket

client = socket.socket()
client.connect(("localhost", 5000))

frames = input("Enter total frames: ")

client.send(frames.encode())

result = client.recv(10000).decode()
print("\nResult:\n")
print(result)

client.close()