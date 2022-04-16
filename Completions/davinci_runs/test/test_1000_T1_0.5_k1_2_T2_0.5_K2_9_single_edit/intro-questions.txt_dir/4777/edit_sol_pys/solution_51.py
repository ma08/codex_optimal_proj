

def fib(n):
    a = 1
    b = 1
    for i in range(n - 1):
        a, b = b, a + b
    return a

k = int(input())
a = fib(k)
b = fib(k + 1)
print(a, b)
