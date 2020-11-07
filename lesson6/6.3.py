

'''lis1 = [x for x in range(1, 11)]
lis2 = [x**2 for x in range(1, 11)]

lis_tuple = list(zip(lis1, lis2))
print(lis_tuple)'''


result_list = [(x, x**2) for x in range(1, 11)]
print(result_list)