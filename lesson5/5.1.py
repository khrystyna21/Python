import random

lis = []

count = 10

i = 0
while i < count:
    number = random.randint(1, 100)
    lis.append(number)
    i +=1

print(lis)
print('Largest number is', max(lis))   #example 1

lis.sort()
print('Largest number is', lis[-1])    #example 2