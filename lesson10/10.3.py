


class TVController:

    def __init__(self, channel):
        self.channel = channel
        self.number = 0

    def first_channel(self):
        self.number = 0
        return self.channel[self.number]

    def last_channel(self):
        self.number = -1
        return self.channel[self.number]

    def turn_channel(self, N):
        if N in range(1, len(self.channel)+1):
            self.number = N - 1
            return self.channel[self.number]
        else:
            return 'Channel number is out of range'

    def next_channel(self):
        self.number +=1
        return self.channel[self.number % len(self.channel)]

    def previous_channel(self):
        self.number -= 1
        return self.channel[self.number % len(self.channel)]

    def current_channel(self):
        return self.channel[self.number % len(self.channel)]

    def is_exist(self, number_name):
        if number_name in self.channel \
                or number_name in range(1, len(self.channel)+1):
            return 'Yes'
        else:
            return 'No'


channels = ["BBC", "Discovery", "TV1000"]
controller = TVController(channels)

print('First channel:', controller.first_channel())
print('Last channel:', controller.last_channel())
print('Turn on the channel:', controller.turn_channel(2))
print('Next channel:', controller.next_channel())
print('Previous channel:', controller.previous_channel())
print('Current channel: ', controller.current_channel())
print('Does channel exist?', controller.is_exist('BBC'))
print('Does channel exist?', controller.is_exist(4))