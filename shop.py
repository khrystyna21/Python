'''
 Вывести меню:
   1. Приготовить кофе
   2. Хочу орео
   3. Хот-дог
 Сделайте свой выбор: 1,2,3
 Введите сумму денег: 10, 20, 30
'''
coffee_price = 35
oreo_price = 100
hot_dog_price = 75

print('1. Приготовить кофе', '2. Хочу Орео', '3. Хотдог', sep='\n')
is_choice_correct = False
while not is_choice_correct:  # not 1 => False
    choice = input('Make your choice: ')
    if choice != '1' and choice != '2' and choice != '3':
        print('Wrong input')
    else:
        is_choice_correct = True
required_amount = 0
if choice == '1':
    required_amount = coffee_price
elif choice == '2':
    required_amount = oreo_price
elif choice == '3':
    required_amount = hot_dog_price
inserted_total_amount = 0
while inserted_total_amount < required_amount:  # 75 < 75
    amount = input('Insert money: ')
    if not amount.isdigit():
        print('Wrong amount')
        continue
    amount = int(amount)
    inserted_total_amount = inserted_total_amount + amount
    print('inserted_total_amount = ', inserted_total_amount)
if choice == '1':
    rest = inserted_total_amount - coffee_price
    if rest < 0:
        print('Not enough money')
    else:
        print('Your coffee, your rest is: ', rest)
elif choice == '2':
    rest = inserted_total_amount - oreo_price
    if rest < 0:
        print('Not enough money')
    else:
        print('Your Oreo, your rest is : ', rest)
elif choice == '3':
    rest = inserted_total_amount - hot_dog_price
    if rest < 0:
        print('Not enough money')
    else:
        print('Your Hot dog, your rest is : ', rest)