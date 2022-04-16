

b, k, g = map(int, input().split())

if k >= b:
    print(1)
else:
    print(b // (k - 1) + 1 if b % (k - 1) != 0 else b // (k - 1))
