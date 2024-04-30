import socket

HOST_IP = '127.0.0.1'
HOST_PORT = 32000
MAX_DATA_SIZE = 1024

# def socket_receive_all_data(socket, data_len):
#     current_data_len = 0
#     total_data = None
#     print('The totality of the data to be received: ', data_len)
#     while current_data_len < data_len:
#         chunk_len = data_len - current_data_len
#         if chunk_len > MAX_DATA_SIZE:
#             chunk_len = MAX_DATA_SIZE
#         data = socket.recv(chunk_len)
#         print('     The length of the received data: ', len(data))
#         if not data:
#             return None
#         if not total_data:
#             total_data = data
#         else:
#             total_data += data
#         current_data_len += len(data)
#         print('     The length of the remaining data: ', current_data_len, "/", data_len)
#     return total_data

def socket_receive_all_data(socket, data_len):
    data = b''
    # print('The totality of the data to be received: ', data_len)
    while data_len:
        if data_len > MAX_DATA_SIZE:
            packet = socket.recv(MAX_DATA_SIZE)
        else:
            packet = socket.recv(data_len)
        # print('     The length of the received data: ', len(packet))
        if not packet:
            raise Exception('Socket closed')
        data += packet
        data_len -= len(packet)
        # print('     The length of the remaining data:', data_len)
    return data

def socket_send_command_and_recv_data(socket, command):
    if not command:
        return None
    socket.sendall(command.encode())

    data_header = socket_receive_all_data(socket, 13)
    data_len = int(data_header.decode())

    return socket_receive_all_data(socket, data_len)

# server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server = socket.socket()
# already used
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((HOST_IP, HOST_PORT))
# server.listen(1)
server.listen()

print(f'Server listening on {HOST_IP}:{HOST_PORT}')
conn, addr = server.accept()
print(f'Connection established on {addr}')
get_filename = None

while True:
    details = socket_send_command_and_recv_data(conn, 'show')
    if not details:
        break
    try:
        command = input(f'{addr[0]}:{addr[1]} {details.decode()} #\n')
        command_split = command.split(' ')
        if len(command_split) == 2 and command_split[0] == 'get':
            get_filename = command_split[1]
    except KeyboardInterrupt as e:
        print(e)
        break

    data = socket_send_command_and_recv_data(conn, command)
    if not data:
        break
    if get_filename:
        if len(data) == 1 and data == b' ':
            print(f'{get_filename}: No such file or directory')
        else:
            f = open(get_filename, 'wb')
            f.write(data)
            f.close()
            print(f'The file {get_filename} is downloaded successfully')
        get_filename = None
    else:
        print(data.decode())

server.close()
conn.close()
