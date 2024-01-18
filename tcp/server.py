import socketserver
import sys

if len(sys.argv) != 2:
    print("usage: server.py <port>")
    sys.exit(1)

IP = "0.0.0.0"
PORT = int(sys.argv[1])

class MyTCPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        self.data = self.request.recv(1024).strip()
        print(f"{self.client_address[0]}: \"{self.data.decode()}\"")

        self.request.sendall(self.data.upper())


print(f"-=[ SERVER LISTENING ON {IP}:{PORT} ]=-\n")

with socketserver.TCPServer((IP, PORT), MyTCPHandler) as server:
    server.serve_forever()
