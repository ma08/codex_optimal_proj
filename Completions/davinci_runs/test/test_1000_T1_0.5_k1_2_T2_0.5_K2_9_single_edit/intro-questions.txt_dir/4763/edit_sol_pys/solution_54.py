

n = int(input())
if n <= 60:
    print("impossible", end="")
else:
    if n % 3 == 0:
        print("triple", n // 3, end="")
        print("triple", n // 3, end="")
        print("triple", n // 3, end="")
    elif n % 3 == 1:
        print("triple", n // 3 - 1, end="")
        print("triple", n // 3 - 1, end="")
        print("double", n // 3 + 6, end="")
    else:
        print("triple", n // 3 - 1, end="")
        print("triple", n // 3 - 1, end="")
        print("single", n // 3 + 7, end="")
