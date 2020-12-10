

def in_range(start, stop = None, step = None):
    if stop == None:
        stop = start
        start = 0

    if step == None:
        step = 1
    elif step == 0:
        raise ValueError ('range() arg 3 must not be zero')

    while True:
        if step > 0 and start >= stop:
            break
        elif step < 0 and start <=stop:
            break
        yield start
        start = start + step


my_list = in_range(1, 10, 1)
my_list1 = in_range(10, -1, -1)
#my_list2 = in_range(1, 10, 0)

for num in my_list:
    print(num)

