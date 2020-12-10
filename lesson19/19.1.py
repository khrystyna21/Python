
from datetime import datetime
import time

class OpenFile():

    counter = 0

    def __init__(self, file_name, mode):
        OpenFile.counter += 1
        self.file_obj = open(file_name, mode)
        now = datetime.now()
        self.logger = now.strftime("%d/%m/%Y %H:%M:%S")

    def __enter__(self):
        print('Open file at', self.logger)
        return self.file_obj

    def __exit__(self, exc_type, exc_value, exc_traceback):
        print('Closing file at {}, number of context: {}'.format(self.logger, self.counter))
        self.file_obj.close()




with OpenFile('test.txt', 'w') as f:
    f.write('Test')


time.sleep(1)


with OpenFile('test.txt', 'r') as f:
    data = f.read()
print(data)

# print(f.closed)

