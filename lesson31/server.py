import socket

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('127.0.0.1', 65432)
print('starting up on {} port {}'.format(*server_address))
socket.bind(server_address)

socket.listen(1)


def get_ansver(data):
    correct_message = "User passed authentification!"
    wrong_message = "Unknown User"

    if data.decode("utf-8") == 'Hello':
        # return correct_message.encode(correct_message, "utf-8")
        return correct_message
    else:
        # return wrong_message.encode(wrong_message, "utf-8")
        return wrong_message


while True:
    # Wait for a connection
    print('waiting for a connection')
    connection, client_address = socket.accept()
    try:
        print('connection from', client_address)

        # Receive the data in small chunks and retransmit it
        while True:
            data = connection.recv(1024)

            print("I get from client - ", repr(data), "\n")

            if data:
                ansver = get_ansver(data)
                message = str.encode(ansver, "utf-8")
                print("I send back to client - ", ansver, "\n")
                # connection.sendall(ansver)
                connection.sendall(message)
            else:
                print('No data from client', client_address)
                break

    finally:
        # Clean up the connection
        connection.close()
