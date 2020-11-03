

import random

user_num = int(input('Enter the number from 1 to 10 '))

if 1 <= user_num <= 10:
    computer_num = random.randint(1, 10)
    if user_num == computer_num:
        print('Your guess is correct')
    else:
        print('Your guess is wrong, the correct answer was', computer_num)
else:
    print('You entered the wrong number')


