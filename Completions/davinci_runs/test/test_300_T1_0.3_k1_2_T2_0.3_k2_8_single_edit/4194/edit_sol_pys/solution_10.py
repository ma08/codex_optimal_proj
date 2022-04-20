

n, m = map(int, input().split())
a = list(map(int, input().split()))
a.sort()

print(n - sum(a)) if a[-1] <= n else print(-1)
