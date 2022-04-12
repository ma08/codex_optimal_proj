

# Solution 1

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

n = int(input()) # input

print(factorial(n) // (factorial(n // 2) ** 2)) # output


# Solution 2

n = int(input()) # input

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(n) // (factorial(n // 2) ** 2))
