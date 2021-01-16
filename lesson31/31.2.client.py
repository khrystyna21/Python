import json
import socket
import random
import time

HOST = '127.0.0.1'
PORT = 65430

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as socket:
    socket.connect((HOST, PORT))

    def send_data():
        x = {"key": random.randint(0, 100),
             "message": input('Input the string ')}

        new_json_str = json.dumps(x)
        message = str.encode(new_json_str, "utf-8")
        print("I send back to server - ", message)

        socket.sendall(message)
        data = socket.recv(1024)
        print("I get from server - ", repr(data), "\n")

    while True:
        time.sleep(1.5)
        send_data()
