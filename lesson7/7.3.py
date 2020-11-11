

def make_operation(operator, *args):
    if operator == '+':
        return_value = 0
        for num in args:
            return_value += num
        return return_value
    elif operator == '-':
        return_value = args[0]
        for num in args[1:]:
           return_value = return_value - num
        return return_value
    elif operator == '*':
        return_value = 1
        for num in args:
            return_value = num * return_value
        return return_value

print(make_operation('+', 7, 7, 2))
print(make_operation('-', 5, 5, -10, -20))
print(make_operation('*', 7, 6))