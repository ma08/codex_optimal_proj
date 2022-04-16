

n = int(input())
if n <= 60:
    print("impossible")
else:
    if n % 3 == 0:
        print("triple " + str(n // 3))
        print("triple " + str(n // 3))
        print("triple " + str(n // 3))
    elif n % 3 == 1:
        print("triple " + str(n // 3 - 1))
        print("triple " + str(n // 3 - 1))
        print("double " + str(n // 3 + 6))
    else:
        print("triple " + str(n // 3 - 1))
        print("triple " + str(n // 3 - 1))
        print("single " + str(n // 3 + 7))
