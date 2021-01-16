import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ('127.0.0.1', 65433)
message = 'This is the message.'

sent = sock.sendto(str.encode(message), server_address)
data, server = sock.recvfrom(1024)
print(data)

sock.close()
