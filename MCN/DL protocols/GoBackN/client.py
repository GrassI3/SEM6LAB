import socket

client = socket.socket()
client.connect(("localhost", 5000))

frames = input("Enter number of frames: ")
window = input("Enter window size: ")

client.send(f"{frames} {window}".encode())

result = client.recv(10000).decode()
print("\nResult:\n")
print(result)

client.close()