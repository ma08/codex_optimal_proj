

def f(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return f(n-1) + f(n-2)

def fib(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a+b
    return a

print(fib(5))
