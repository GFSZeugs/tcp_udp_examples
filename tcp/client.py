import socket
import sys

if len(sys.argv) != 2:
    print("usage: client.py <server_ip>:<server_port>")
    sys.exit(1)

SERVER_IP, SERVER_PORT = sys.argv[1].split(":")

data = "Hallo, ich bin eine Testnachricht!"

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    # Connect to server and send data
    sock.connect((SERVER_IP, int(SERVER_PORT)))
    sock.sendall(bytes(data + "\n", "utf-8"))

    # Receive data from the server and shut down
    received = str(sock.recv(1024), "utf-8")

print(f"Sent:     {data}")
print(f"Received: {received}")
