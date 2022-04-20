

n, m = map(int, input().split())
a = list(map(int, input().split())) + [0]

ans = 0
cur = 0
for i in range(m):
    cur += a[i]
    if cur >= n:
        ans += 1
        cur = 0

for i in range(m, len(a)):
    cur += a[i] - a[i - m]
    if cur >= n:
        ans += 1
        cur = 0

print(ans)
