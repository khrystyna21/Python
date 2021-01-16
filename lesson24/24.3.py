class Stack:
    def __init__(self):
        self.stack = []

    def isEmpty(self):
        return self.stack == []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if len(self.stack) < 1:
            return None
        return self.stack.pop()

    def size(self):
        return len(self.stack)

    def get_from_stack(self, element):
        if element in self.stack:
            pos = self.stack.index(element)
            return self.stack.pop(pos)
        else:
            raise ValueError('There is no such element in a stack')

    def __str__(self):
        return str(self.stack)


# my_stack = Stack()
# my_stack.push('cherry')
# my_stack.push('apple')
# my_stack.push('honey')
#
# print(my_stack)
# print(my_stack.get_from_stack('apple'))
# print(my_stack)
# print(my_stack.get_from_stack('mango'))


class Queue:

    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)
        # self.queue.insert(0,item)

    def dequeue(self):
        if len(self.queue) < 1:
            return None
        return self.queue.pop(0)

    def size(self):
        return len(self.queue)

    def get_from_queue(self, element):
        if element in self.queue:
            pos = self.queue.index(element)
            return self.queue.pop(pos)
        else:
            raise ValueError('There is no such element in a queue')

    def __str__(self):
        return str(self.queue)

my_queue = Queue()
my_queue.enqueue('cherry')
my_queue.enqueue('apple')
my_queue.enqueue('honey')

print(my_queue)
print(my_queue.get_from_queue('apple'))
print(my_queue)
print(my_queue.get_from_queue('mango'))