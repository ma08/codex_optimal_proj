

q = int(input())
for i in range(q):
    n, a, b = map(int, input().split())
    m = min(a, b)
    M = max(a, b)
    if n == 1:
        print(m)
    else:
        if n % 2 == 0:
            print((n // 2) * m)
        else:
            print((n // 2) * m + m)