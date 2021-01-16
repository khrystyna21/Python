from collections import deque


open_list = ["[", "{", "("]
close_list = ["]", "}", ")"]


def balance(str):
    my_stack = deque()
    for i in str:
        if i in open_list:
            my_stack.append(i)
        elif i in close_list:
            pos = close_list.index(i)
            if ((len(my_stack) > 0) and
                    (open_list[pos] == my_stack[len(my_stack) - 1])):
                my_stack.pop()
            else:
                return "Unbalanced"
    if len(my_stack) == 0:
        return "Balanced"
    else:
        return "Unbalanced"


print(balance('[{())}]'))
print(balance('([)]'))