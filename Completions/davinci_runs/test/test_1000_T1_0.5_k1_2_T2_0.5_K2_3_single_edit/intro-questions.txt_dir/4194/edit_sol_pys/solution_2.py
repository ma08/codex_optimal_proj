

n, m = map(int, input().split())
a = list(map(int, input().split()))
a.sort()

s = 0
for i in range(m - 1):
    if a[i + 1] - a[i] > 1:
        s += a[i]
        break
else:
    s += a[m - 1]

print(n - s)
