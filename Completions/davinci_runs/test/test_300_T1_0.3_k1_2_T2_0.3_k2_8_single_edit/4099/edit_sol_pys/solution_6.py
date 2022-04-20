

n, k, m = map(int, input().split())
a = list(map(int, input().split()))

if sum(a) / n >= m:
    print(-1)
else:
    print(max(0, m * n - sum(a)))
