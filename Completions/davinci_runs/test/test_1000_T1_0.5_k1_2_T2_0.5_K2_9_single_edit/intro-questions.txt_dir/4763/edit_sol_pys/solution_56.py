
n = int(input())

if n % 3 == 0 and n % 2 == 0:
    print("triple double", n // 3, n // 2)
elif n % 3 == 0:
    print("triple single", n // 3, n)
elif n % 2 == 0:
    print("double single", n // 2, n)
else:
    print("single", n)
