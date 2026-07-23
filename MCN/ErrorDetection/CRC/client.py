import socket

client = socket.socket()
client.connect(("localhost", 5000))

data = input("Enter Data bits: ")
gen = input("Enter Generator bits: ")

client.send(f"{data} {gen}".encode())

result = client.recv(1024).decode()
print("\nResult:\n")
print(result)

client.close()