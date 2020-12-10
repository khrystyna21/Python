

def with_index(sequence, start=0):
    for i in range(len(sequence)):
        yield start+i, sequence[i]


objects = ['pen', 'book', 'cup']
enumerate_list = list(with_index(objects))

print(enumerate_list)
