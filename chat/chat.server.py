from concurrent.futures import ThreadPoolExecutor
import json_test
import socket

'''
    1). Должен уметь оркестрировать сообщение - от кого и кому
    2). Должен хранить всех подключенных клиентов (адрессатов)
    3). Уведомлять всех клиентов о каких-то событиях (например, новое подключение)

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('', 8887))
    s.listen(5)

try:
    while True:
        print('in cycle')
        client, addr = s.accept()
        # Принять запрос на соединение
        print("Получен запрос на соединение с %s" % str(addr))
        timestr = "Текущее время: %s" % time.ctime(time.time()) + "\r\n"
        encoded_time = timestr.encode('utf-8')
        client.send(encoded_time)
        client.close()


'''


class ChatServer:
    def __init__(self, host='', port=8088, max_clients=5):
        self.host = host
        self.port = port
        self.max_clients = max_clients
        self._s = None
        self._users = {}
        self._executor = ThreadPoolExecutor(max_workers=max_clients)

    def prepare_message(self, message):
        return json_test.dumps(message).encode('utf-8')

    def parse_message(self, message, client):
        message = json_test.loads(message.decode('utf-8'))
        if message['message_type'] == 'service':
            if message['message'] == 'HELLO':
                current_users = list(self._users.keys())
                self._users[message['client_id']] = client
                print('New user added, current_users: ', list(self._users.keys()))
                response_message = {
                    'message_type': 'service',
                    'message': 'CURRENT_USERS',
                    'payload': current_users
                }
                client.sendall(self.prepare_message(response_message))
                for client_id in self._users:
                    if client_id != message['client_id']:
                        self._users[client_id].sendall(
                            self.prepare_message({
                                'message_type': 'service',
                                'message': 'NEW_USER',
                                'payload': message['client_id']
                            })
                        )
                self._executor.submit(self.client_listener, message['client_id'])
        elif message['message_type'] == 'custom':
            recipient = message['recipient']
            sender = message['client_id']
            payload = message['message']
            new_message = {
                'message_type': 'custom',
                'client_id': sender,
                'message': payload
            }
            recipient_client = self._users[recipient]
            print('sending to %s, message %s' % (recipient, new_message))
            recipient_client.sendall(self.prepare_message(new_message))

    def client_listener(self, client_id):
        client = self._users[client_id]
        while True:
            message = client.recv(8192)
            if not message:
                for item in self._users:
                    if item != client_id:
                        self._users[item].sendall(
                            self.prepare_message({
                                'message_type': 'service',
                                'message': 'USER_LEFT',
                                'payload': item
                            })
                        )
                break
            print('New message from %s: %s' % (client_id, message))
            self.parse_message(message, client)

    def start(self):
        self._s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._s.bind((self.host, self.port))
        self._s.listen(self.max_clients)
        while True:
            client, addr = self._s.accept()
            message = client.recv(8192)
            print('NEW message: ', message)
            self.parse_message(message, client)


if __name__ == '__main__':
    server = ChatServer()
    server.start()


