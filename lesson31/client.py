import socket
import random
import time

# python client.py

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432  # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as socket:
    def get_message(choice):
        if choice is True:
            return 'Hello'
        else:
            return 'Hi'


    def send_data():
        choice = random.choice([True, False])
        message = get_message(choice)
        message = str.encode(message, "utf-8")

        print("I send tp server - ", message, "\n")
        socket.sendall(message)
        data = socket.recv(1024)
        print("I get from server - ", repr(data), "\n")


    socket.connect((HOST, PORT))
    while True:
        time.sleep(2)
        send_data()
