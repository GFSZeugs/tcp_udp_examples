import socket
import sys

if len(sys.argv) != 2:
    print("usage: server.py <port>")
    sys.exit(1)

IP = "0.0.0.0"
PORT = int(sys.argv[1])

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 

sock.bind((IP, PORT))

print(f"-=[ SERVER LISTENING ON {IP}:{PORT} ]=-\n")

while True:
    try:
        data, addr = sock.recvfrom(1024)
        sender_ip, sender_port = addr
        print(f"{sender_ip}: \"{data.decode()}\"")
    except:
        print("Invalide Nachricht")
