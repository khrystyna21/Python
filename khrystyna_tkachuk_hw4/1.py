# task 1

def replace_symbol(str):
    new_str = str.replace('"', '\'')
    return new_str

string = ''' "I python you" '''
print(replace_symbol(string))