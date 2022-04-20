

n, m = map(int, input().split())
a = list(map(int, input().split()))

a.sort()

if a[-1] > n:
    print(-1)
else:
    print(n - sum(a))