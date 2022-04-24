
a = int(input())
# a = 3

def factorial(a):
    if a == 1:
        return 1
    else:
        return a * factorial(a-1)

res = factorial(a)
print(res)
