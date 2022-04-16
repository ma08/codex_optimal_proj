

def fib(n):
    a = 1
    b = 1
    for i in range(n - 1):
        a, b = b, a + b
    return b

k = int(input())
b = fib(k)
print(b)
