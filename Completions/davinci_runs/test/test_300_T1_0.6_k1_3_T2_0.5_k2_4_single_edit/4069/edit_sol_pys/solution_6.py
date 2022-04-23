

x, k, d = map(int, input().split())

if (k * d) > x:
    print(abs(x - (k * d)))
else:
    k = k - (x // d)
    x = x % d
    if k % 2 == 0:
        print(abs(x))
    else:
        print(abs(x - d))
