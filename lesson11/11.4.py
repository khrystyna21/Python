
from datetime import datetime

class CustomException(Exception):

    def __init__(self, msg):
        super().__init__(msg)
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        self.f = open ('logs.txt', 'a')
        self.f.write('Error: ' + dt_string + ' ' + str(msg))
        self.f.close()


number = 25

string = input('Enter your code ')
if len(string) > number:
    raise CustomException('Your code is too long\n')

