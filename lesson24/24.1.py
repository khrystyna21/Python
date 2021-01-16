from collections import deque


def reverse_stack(str):
    my_stack = deque()
    length = len(str)
    for i in range(0, length):
        my_stack.append(str[i])
    str = ''
    for i in range(0, length):
        str += my_stack.pop()
    return str

str = 'Python'
str = reverse_stack(str)
print(str)