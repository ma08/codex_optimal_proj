


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

for _ in range(int(input())):
    print(factorial(int(input())) % 10)
