import socket
import time

HOST_IP = "127.0.0.1"
HOST_PORT = 32000
MAX_DATA_SIZE = 1024

# Connect to server
while True:
    try:
        # Create socket client
        client = socket.socket()
        print(f"Connect to server {HOST_IP}:{HOST_PORT}")
        client.connect((HOST_IP, HOST_PORT))
    except ConnectionRefusedError as e:
        print(f"ERROR: Connection refused to server {HOST_IP}:{HOST_PORT} - Retry connection...")
        time.sleep(4)
    else:
        print("Connection established")
        break

while True:
    # Receive data from server
    data = client.recv(MAX_DATA_SIZE)
    if not data:
        break
    print(f"Mesage: {data.decode()}")
    send_message = input("Vous: ")
    client.sendall(send_message.encode())

# Close the socket
client.close()
