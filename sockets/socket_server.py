import socket

HOST_IP = "127.0.0.1"
HOST_PORT = 32000
MAX_DATA_SIZE = 1024

# server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server = socket.socket()
# already used
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((HOST_IP, HOST_PORT))
# server.listen(1)
server.listen()

print(f"Server listening on {HOST_IP}:{HOST_PORT}")
conn, addr = server.accept()
print(f"Connection established on {addr}")

while True:
    send_message = input("Vous: ")
    conn.sendall(send_message.encode())
    data = conn.recv(MAX_DATA_SIZE)
    if not data:
        break
    print(f"Message: {data.decode()}")

server.close()
conn.close()
