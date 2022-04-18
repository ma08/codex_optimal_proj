
n = int(input())

if n % 3 == 0:
    print("triple", n // 3)  # triple 1
elif n % 2 == 0:
    print("double", n // 2)  # double 2
else:
    print("single", n)  # single 5
