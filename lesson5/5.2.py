import random

lis1 = []
lis2 = []

i = 0
while i < 10:
    number = random.randint(1, 10)
    lis1.append(number)
    i +=1

print(lis1)

i = 0
while i < 10:
    number = random.randint(1, 10)
    lis2.append(number)
    i +=1

print(lis2)

set = set(lis1) & set(lis2)
lis3 = list(set)

print(lis3)