

def count_lines(name):
    f = open(name, "r")
    return len(f.readlines())

def count_chars(name):
    f = open(name, "r")
    data = f.read()
    number_of_chr = len(data)
    return number_of_chr

# print(count_lines('test.txt'))
# print(count_chars('test.txt'))