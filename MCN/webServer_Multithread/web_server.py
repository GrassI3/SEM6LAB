import socket

server = socket.socket()
server.bind(("localhost", 8080))
server.listen(5)

print("Web Server Running...")

while True:
    conn, addr = server.accept()
    print("Connected:", addr)

    conn.recv(1024)   # Receive request

    response = """HTTP/1.1 200 OK

<html>
<head><title>Web Server</title></head>
<body>
<h1>Hello from Python Web Server!</h1>
</body>
</html>
"""

    conn.send(response.encode())
    conn.close()