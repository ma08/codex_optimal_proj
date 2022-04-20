
a = int(input())
# a = 3

def factorial(n):
    return n * factorial(n-1) if n > 1 else 1

res = factorial(a)
print(res)
