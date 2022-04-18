
t = int(input())
for i in range(t):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    p = list(map(int, input().split()))
    k = set()
    for j in range(m):
        k.add(p[j] - 1)
    for j in range(n - 1):
        if j in k:
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
    k = True
    for j in range(n - 1):
        if a[j] > a[j + 1]:
            k = False
            break
    if k:
        print("YES")
    else:
        print("NO")
