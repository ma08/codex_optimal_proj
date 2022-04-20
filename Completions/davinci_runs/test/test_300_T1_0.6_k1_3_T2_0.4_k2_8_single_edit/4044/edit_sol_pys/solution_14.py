
a, b, x = map(int, input().split())

if (a - x) >= b:
    print("0" * x + "1" * b)
elif (b - x) >= a:
    print("1" * x + "0" * a)
else:
    zeros = a - (x - b)
    print("1" * (x - zeros) + "0" * zeros + "1" * b)
