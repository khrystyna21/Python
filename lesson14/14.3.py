
from functools import wraps




def arg_rules(max_length, type_, contains):
    def arg_rules_dec(func):
        @wraps(func)
        def wrap(name):
            if len(str(name)) > max_length:
                print('Name is too long')
                return False
            elif isinstance(name, type_) is False:
                print('Name is not a string')
                return False
            elif any(item not in name for item in contains):
                print("Name doesn't contain symbols")
                return False
            else:
                return func(name)
        return wrap
    return arg_rules_dec



@arg_rules(type_=str, max_length=15, contains=['05', '@'])
def create_slogan(name):
    return f'{name} drinks pepsi in his brand new BMW!'


print(create_slogan('johndoe05@gmail.com'))
print(create_slogan('S@SH05'))




