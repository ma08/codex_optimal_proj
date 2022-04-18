

def fib(n):
    a = 1
    b = 1
    for i in range(n - 1):
        a, b = b, a + b
    return a, b



k = int(input())
a, b = fib(k)
print(a, b)
