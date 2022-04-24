

n, m = map(int, input().split())

if (n + m) % 2 == 0 and n > 0 and m > 0:
    print(2 ** (n + m) - 2 ** ((n + m) // 2) - 1)
else:
    print(2 ** (n + m))
