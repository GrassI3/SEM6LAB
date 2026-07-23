import socket
import threading

def handle_client(conn):
    request = conn.recv(1024)

    client = socket.socket()
    client.connect(("localhost", 8080))   # Connect to web server
    client.send(request)

    response = client.recv(4096)

    conn.send(response)

    client.close()
    conn.close()

proxy = socket.socket()
proxy.bind(("localhost", 9090))
proxy.listen(5)

print("Proxy Server Running...")

while True:
    conn, addr = proxy.accept()
    print("Connected:", addr)

    threading.Thread(target=handle_client, args=(conn,)).start()