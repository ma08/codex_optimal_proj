

n = int(input("enter a number: "))

if n % 3 == 0:
    print("triple", n // 3, " = ", n)
elif n % 2 == 0:
    print("double", n // 2, " = ", n)
else:
    print("single", n)
