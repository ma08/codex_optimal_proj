a = int(input())

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

res = factorial(a)
print(res)
