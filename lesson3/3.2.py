

number = input('Enter your phone number: ')

if number.isdigit() is False:
    print('Wrong characters')
elif len(number) < 10:
    print('Not enough numbers')
else:
    print('Thanks, we will call you')
