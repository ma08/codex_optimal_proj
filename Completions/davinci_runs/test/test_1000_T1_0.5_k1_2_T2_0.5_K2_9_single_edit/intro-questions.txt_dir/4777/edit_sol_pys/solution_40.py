

def fib(n):
    if n == 1:
        return 1
    else:
        return n * fib(n - 1)

k = int(input())
a, b = fib(k)
print(a, b)
