# task 1

n = int(input('Enter number '))
if n > 0:
    res = n**2
elif n < 0:
    res = abs(n)
else:
    res = 0

print('result =', res)