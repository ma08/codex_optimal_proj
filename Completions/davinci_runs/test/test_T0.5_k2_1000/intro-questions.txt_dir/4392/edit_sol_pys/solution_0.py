
t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    p = list(map(int, input().split()))

    a.sort()
    for i in range(m - 1):
        if p[i] + 1 == p[i + 1]:
            a[p[i]], a[p[i] + 1] = a[p[i] + 1], a[p[i]]
    print("YES" if all(a[i] <= a[i + 1] for i in range(n - 1)) else "NO")
