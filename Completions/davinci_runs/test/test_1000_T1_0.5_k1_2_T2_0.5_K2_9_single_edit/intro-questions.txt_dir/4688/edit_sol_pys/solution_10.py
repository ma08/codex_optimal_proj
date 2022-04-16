

n, k = map(int, input().split())

if n == 1:
    print(k)
else:
    if n == 2:
        print(k * (k - 1))
    else:
        print(k * (k - 1) ** (n - 1))
