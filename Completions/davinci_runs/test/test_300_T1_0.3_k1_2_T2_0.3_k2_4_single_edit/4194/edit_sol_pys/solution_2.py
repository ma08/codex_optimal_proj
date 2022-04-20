
n, m = map(int, input().split())
a = list(map(int, input().split()))

a.sort()

if a[-1] > m:
    print(-1)
else:
    print(m - sum(a))
