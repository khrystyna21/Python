import json_test
import socket

'''
    1) Подключается к серверу
    2) Получает сервисную информацию (кол-во пользователей, их имена)
    3) Отсылает данные

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('localhost', 8887))
'''


class ChatClient:
    def __init__(self, client_id, host='', port=8088):
        self.client_id = client_id
        self.host = host
        self.port = port
        self._s = None

    def _prepare_message(self, message):
        message['client_id'] = self.client_id
        return json_test.dumps(message).encode('utf-8')

    def send_greeting_message(self):
        message = {
            'message_type': 'service',
            'message': 'HELLO'
        }
        self._s.sendall(self._prepare_message(message))

    def send_custom_message(self, message_str):
        # dima:Hello and soon...
        message_attrs = message_str.split(':')
        recipient = message_attrs[0]
        message = message_attrs[1]
        message = {
            'message_type': 'custom',
            'recipient': recipient,
            'message': message
        }
        self._s.sendall(self._prepare_message(message))

    def parse_response(self, response):
        message = json_test.loads(response.decode('utf-8'))
        print('raw message: ', message)
        if message['message_type'] == 'service':
            if message['message'] == 'CURRENT_USERS':
                print('Current users: ', message['payload'])
            if message['message'] == 'NEW_USER':
                print('New user added: ', message['payload'])
            if message['message'] == 'USER_LEFT':
                print('USER LEFT: ', message['payload'])
        if message['message_type'] == 'custom':
            client_id = message['client_id']
            print('New message from %s: >> %s <<' % (client_id, message['message']))

    def start(self):
        self._s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._s.connect((self.host, self.port))
        self.send_greeting_message()
        response = self._s.recv(8192)
        self.parse_response(response)
        while True:
            message = input('Enter message (empty to wait for): ')
            if not message:
                response = self._s.recv(8192)
                self.parse_response(response)
            else:
                self.send_custom_message(message)
                response = self._s.recv(8192)
                self.parse_response(response)


if __name__ == '__main__':
    client = ChatClient(client_id='igor')
    client.start()

