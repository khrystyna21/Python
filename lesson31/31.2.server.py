import json
import socket

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('127.0.0.1', 65430)
print('starting up on {} port {}'.format(*server_address))
socket.bind(server_address)

socket.listen(1)


def encrypt(text, s):
    result = ""
    for i in range(len(text)):
        char = text[i]
        if (char.isupper()):
            result += chr((ord(char) + s - 65) % 26 + 65)
        else:
            result += chr((ord(char) + s - 97) % 26 + 97)
    return result


while True:
    print('waiting for a connection')
    connection, client_address = socket.accept()
    try:
        print('connection from', client_address)

        while True:
            data = connection.recv(1024)

            print("I get from client ", repr(data))

            if data:
                message = data.decode("utf-8")
                y = json.loads(message)

                key = y["key"]
                msg = y["message"]

                answer = encrypt(msg, key)
                message = str.encode(answer, "utf-8")

                print("I send back to client - ", answer, '\n')
                connection.sendall(message)
            else:
                print('No data from client', client_address)
                break

    finally:
        connection.close()
