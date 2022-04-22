n = int(input())
a = [int(x) for x in input().split()]

b = []
for i in range(n):
    if i == 0:
        b.append(a[i])
    else:
        b.append(b[i - 1] + a[i])

print(b)

c = []
for i in range(n):
    if i == n - 1:
        c.append(a[i])
    else:
        c.append(c[i - 1] + a[i])

print(c)
