import socket

HOST = "127.0.0.1"
PORT = 65433

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((HOST, PORT))

print("UDP server up and listening")

while True:
    data, address = sock.recvfrom(1024)
    print('received %s bytes from %s' % (len(data), address))
    if not data:
        break
    sent = sock.sendto(data, address)
    print('sent %s bytes back to %s' % (sent, address))


