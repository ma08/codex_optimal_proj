

n = int(input())
if n <= 60:
    print("impossible")
else:
    if n % 3 == 0:
        print("triple", n // 3, "triple", n // 3, "triple", n // 3)
    elif n % 3 == 1:
        print("triple", n // 3, "triple", n // 3, "double", n // 3 + 6)
    else:
        print("triple", n // 3, "triple", n // 3, "single", n // 3 + 7)
