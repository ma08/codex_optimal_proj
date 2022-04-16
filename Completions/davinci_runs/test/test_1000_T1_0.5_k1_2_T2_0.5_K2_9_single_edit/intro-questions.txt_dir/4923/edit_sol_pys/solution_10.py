
n = int(input())
a = list(map(int, input().split()))

c = [0] * 7
for i in range(n):
    c[a[i]] += 1
    if c[a[i]] > 1:
        c[a[i]] = -1

m = max(c)
if m == 0:
    print(0)
else:
    print(c.index(m))
