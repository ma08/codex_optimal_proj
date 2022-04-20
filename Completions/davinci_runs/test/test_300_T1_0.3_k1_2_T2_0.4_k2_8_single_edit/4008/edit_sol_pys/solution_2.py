
n, k = map(int, input().split())
a = list(map(int, input().split()))

if k > n:
    print("NO")
elif k == n:
    print("YES")
    print(*[i for i in range(1, k + 1)]
else:
    d = {}
    for i in range(n):
        if a[i] not in d:
            d[a[i]] = []
        d[a[i]].append(i)
    if len(d) < k:
        print("NO")
    else:
        print("YES")
        c = [0] * n
        for i in range(1, k + 1):
            if i <= len(d):
                c[d[i][0]] = i
            else:
                c[d[1][i - len(d)]] = i
        print(*c
