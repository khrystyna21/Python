# task 2
import random
n = random.randint(100, 999)
print('n =', n)
list = [int(i) for i in str(n)]
for i in range(len(list)):
    for j in range(0, len(list) - i - 1):
        if list[j] < list[j + 1]:
            list[j], list[j + 1] = list[j + 1], list[j]
res = int("".join(map(str, list)))

print('result =', res)