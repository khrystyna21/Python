
import random
range_begin = round(random.randint(1, 1000), -2)
range_end = range_begin + 100
print(
    '''Please remember a number in range
     from {} to {} and I will guess it'''.format(
        range_begin, range_end
    )
)
input('Lets start ?')
while True:
    print('Is your number equal to {} ?'.format(
        (range_end + range_begin) // 2)
    )
    answer = input('Answer please as: \n 1. Equal \n 2. Less \n 3. Greater: ')
    if answer != '1' and answer != '2' and answer != '3':
        print('Wrong input, please retry.')
        continue
    if answer == '1':
        print('Great')
        break
    elif answer == '2':
        range_end = (range_end + range_begin) // 2
    elif answer == '3':
        range_begin = (range_end + range_begin) // 2