


def func(a, b):
    try:
        a = int(a)
        b = int(b)
        return (a**2)/b
    except ValueError:
        return 'Only numbers are allowed'
    except ZeroDivisionError:
        return 'Division by 0 is not allowed'

a = input('Enter first number: ')
b = input('Enter second number: ')

print(func(a, b))


