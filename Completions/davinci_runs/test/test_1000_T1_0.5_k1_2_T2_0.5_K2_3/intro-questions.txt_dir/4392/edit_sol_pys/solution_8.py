t = int(input())
for i in range(t):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    p = list(map(int, input().split()))
    s = set()
    for j in range(m):
        s.add(p[j] - 1)
    for j in range(n - 1):
        if j in s:
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
    f = True
    for j in range(n - 1):
        if a[j] > a[j + 1]:
            f = False
            break
    if f:
        print("YES")
    else:
        print("NO")
