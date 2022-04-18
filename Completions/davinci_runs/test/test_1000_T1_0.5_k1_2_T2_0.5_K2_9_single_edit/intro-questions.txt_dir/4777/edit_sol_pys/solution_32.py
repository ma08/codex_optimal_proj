

def fib(n):
    a = 1
    b = 1
    for i in range(n - 2):
        a, b = b, a + b
    return b

k = int(input())
print(fib(k))
