
n, m = map(int, input().split())
a = list(map(int, input().split()))
a.sort()

if a[-1] > n:
    print(-1)
    exit()

s = 0
for i in range(m):
    s += a[i]

print(n - s)
