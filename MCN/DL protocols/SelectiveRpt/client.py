import socket

client = socket.socket()
client.connect(("localhost", 5000))

frames = input("Enter frames and window size: ").split()

client.send(f"{frames[0]} {frames[1]}".encode())

result = client.recv(10000).decode()
print(result)

client.close()