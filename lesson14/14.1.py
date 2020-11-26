

from functools import wraps


def logger(func):
    @wraps(func)
    def wrapper(*args):
        result = func(*args)
        print(func.__name__ + ' called with', args)
        return result
    return wrapper


@logger
def add(x, y):
    return x + y


@logger
def square_all(*args):
    return [arg ** 2 for arg in args]

print(add(4, 5))
print(square_all(5, 8))