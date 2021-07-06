# task4

n = int(input('Write n: '))
if n > 0:
    binary = bin(n)[2:]
    res = 0
    for i in binary:
        if int(i) == 1:
            res += int(i)

print('n =', n, '=', binary, 'result =', res)