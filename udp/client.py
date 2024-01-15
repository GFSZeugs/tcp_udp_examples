import socket
import sys


if len(sys.argv) != 2:
    print("usage: client.py <server_ip>:<server_port>")
    sys.exit(1)

SERVER_IP, SERVER_PORT = sys.argv[1].split(":")

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print(f"-=[ CLIENT SENDING TO {SERVER_IP}:{SERVER_PORT} ]=-\n")

while True:
    msg = input("Enter a message: ")
    code = sock.sendto(msg.encode(), (SERVER_IP, int(SERVER_PORT)))
