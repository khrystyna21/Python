
'''x = range(1, 101)

lis = list(x)
print(lis)'''

lis = []
x1 = 1
x2 = 100

while x1 <= x2:
    lis.append(x1)
    x1 +=1
print(lis)

new_lis = []
len = len(lis)

i = 0
while i < len:
    if (i%7 == 0) and (i%5 != 0):
        new_lis.append(i)
    i +=1
print(new_lis)