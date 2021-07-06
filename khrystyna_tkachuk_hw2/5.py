# task5

n = int(input('Write n: '))

def Fibonacci(n):
    if n > 0:
        fibo = [0] * n
        fibo[1] = 1
        sum = fibo[0] + fibo[1]
        for i in range(2, n):
            fibo[i] = fibo[i - 1] + fibo[i - 2]
            sum = sum + fibo[i]
        return sum

print(Fibonacci(n))

