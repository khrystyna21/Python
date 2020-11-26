

def calculator(x):
    def adding(y):
        return x+y
    return adding

result = calculator(5)(10)
print(result)