
a, b = map(int, input().split())

if a % 2 == 0:
    if b % 2 == 0:
        print("Even")
    else:
        print("Odd")
else:
    if b % 2 == 0:
        print("Odd")
    else:
        print("Even")
