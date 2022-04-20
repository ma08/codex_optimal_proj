

# x, k, d = map(int, input().split())
x, k, d = 6, 2, 4

# 1. x >= 0
if x >= 0:
    if x >= k * d:
        print(x - k * d)
    else:
        k -= x // d
        x %= d
        if k % 2 == 0:
            print(x)
        else:
            print(d - x)
# 2. x < 0
else:
    x = -x
    if x >= k * d:
        print(x - k * d)
    else:
        k -= x // d
        x %= d
        if k % 2 == 0:
            print(x)
        else:
            print(d - x)