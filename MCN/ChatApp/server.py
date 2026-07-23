import socket

s = socket.socket()
s.bind(('localhost', 8080))
s.listen(1)

print("Waiting for client...")
conn, addr = s.accept()
print("Client connected!\n")

while True:
    print("Client:", conn.recv(1024).decode())
    msg = input("Server: ")
    conn.send(msg.encode())