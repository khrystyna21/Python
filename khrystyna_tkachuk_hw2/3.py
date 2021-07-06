# task3

n = input('Write n: ')

if int(n) > 0:
    res = 0
    for i in n:
        if int(i) % 2 != 0:
            res += int(i)

print('result =', res)