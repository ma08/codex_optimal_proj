def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)
for _ in range(int(input())):  # number of test cases
    print(factorial(int(input())) % 10)  # get the last digit of the factorial
