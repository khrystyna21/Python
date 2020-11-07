

stock = dict(
    banana = 6,
    apple = 0,
    orange = 32,
    pear = 15
)
prices = dict(
    banana = 4,
    apple = 2,
    orange = 1.5,
    pear = 3
)

total = 0
for i in stock:
    value = prices[i] * stock[i]
    print(value)
    total = total + value
print(total)

