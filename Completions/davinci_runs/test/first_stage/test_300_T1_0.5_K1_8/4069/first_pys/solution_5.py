

x, k, d = map(int, input().split())

if abs(x) >= k * d:
    print(abs(x) - k * d)
else:
    k -= abs(x) // d
    x = abs(x) % d
    if k % 2 == 0:
        print(x)
    else:
        print(abs(x - d))