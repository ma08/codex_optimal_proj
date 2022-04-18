

def factorial(n):
    return 1 if n == 0 else n * factorial(n-1)

for _ in range(int(input())):
    print(factorial(int(input())) % 10)
