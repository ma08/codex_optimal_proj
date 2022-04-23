
# a = int(input())
a = 3

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

result = factorial(a)
print(result)
