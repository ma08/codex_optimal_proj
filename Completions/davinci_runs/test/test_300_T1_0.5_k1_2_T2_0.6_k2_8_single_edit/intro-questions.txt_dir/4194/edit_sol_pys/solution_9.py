

n, m = map(int, input().split())
a = list(map(int, input().split()))

a.sort()
s = 0
for i in range(m):
    s += a[i]

print(n - s)
