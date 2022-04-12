

b, k, g = map(int, input().split())

if k >= b:
    print(1)
else:
    print(b // (g - 1) + 1 if b % (g - 1) != 0 else b // (g - 1))
