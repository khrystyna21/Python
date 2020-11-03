


import random

number_1 = random.randint(1,100)
number_2 = random.randint(1,100)

symbol_correct = False
while not symbol_correct:
    operation = input('''Please type math operation:
+ for addition
- for subtraction
* for multiplication
/ for division 
''')
    if operation != '+' and operation != '-' and operation != '*' and operation != '/':
        print('You have not typed a valid operator, please run the program again.')
    else:
        symbol_correct = True


if operation == '+':
    result_from_computer = number_1 + number_2
    print('{} + {} = '.format(number_1, number_2))
elif operation == '-':
    result_from_computer = number_1 - number_2
    print('{} - {} = '.format(number_1, number_2))
elif operation == '*':
    result_from_computer = number_1 * number_2
    print('{} * {} = '.format(number_1, number_2))
elif operation == '/':
    result_from_computer = number_1 / number_2
    print('{} / {} = '.format(number_1, number_2))


print('Write your answer: ')

answer = int(input('= '))

if int(answer) == result_from_computer:
    print('You are correct. Well done')
else:
    print("Think better. Try again")