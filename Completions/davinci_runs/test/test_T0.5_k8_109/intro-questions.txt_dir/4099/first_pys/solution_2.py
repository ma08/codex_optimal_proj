

n, k, m = map(int, input().split())
a = list(map(int, input().split()))

avg = sum(a) / (n - 1)

if avg >= m:
    print(0)
else:
    print(m * n - sum(a))