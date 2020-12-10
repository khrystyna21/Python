from functools import wraps


class TypeDecorators:

    @staticmethod
    def to_int(func):
        @wraps(func)
        def wrapper(*args):
            result = func(*args)
            return int(result)

        return wrapper

    @staticmethod
    def to_str(func):
        @wraps(func)
        def wrapper(*args):
            result = func(*args)
            return str(result)

        return wrapper

    @staticmethod
    def to_bool(func):
        @wraps(func)
        def wrapper(*args):
            result = func(*args)
            return bool(result)

        return wrapper

    @staticmethod
    def to_float(func):
        @wraps(func)
        def wrapper(*args):
            result = func(*args)
            return float(result)

        return wrapper


@TypeDecorators.to_int
def do_nothing(string):
    return string


print(type(do_nothing('25')))  # перевіряю, чи дійсно змінило на int


@TypeDecorators.to_str
def do_nothing(string):
    return string


print(type(do_nothing(25)))  # перевіряю, чи дійсно змінило на str


@TypeDecorators.to_bool
def do_something(string):
    return string


print(do_something(1))
print(do_something(0))  # оскільки 0 -- завжди False


@TypeDecorators.to_float
def just_do(int):
    return int


print(just_do(1))
