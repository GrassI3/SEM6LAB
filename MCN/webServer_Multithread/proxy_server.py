import socket
import threading

def handle_client(client):
    request = client.recv(1024)

    server = socket.socket()
    server.connect(("localhost", 8080))   # Connect to web server
    server.send(request)

    response = server.recv(4096)

    client.send(response)

    server.close()
    client.close()

proxy = socket.socket()
proxy.bind(("localhost", 9090))
proxy.listen(5)

print("Proxy Server Running...")

while True:
    client, addr = proxy.accept()
    print("Connected:", addr)

    threading.Thread(target=handle_client, args=(client,)).start()