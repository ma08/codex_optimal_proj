
#!/usr/bin/env python2

n = int(input())
a = list(map(int, input().split()))

d = [0] * n

for i in range(n - 1, -1, -1):
    if i + a[i] < n and i - a[i] >= 0:
        d[i] = min(d[i + a[i]] + 1, d[i - a[i]] + 1)
    elif i + a[i] < n:
        d[i] = d[i + a[i]] + 1
    elif i - a[i] >= 0:
        d[i] = d[i - a[i]] + 1
    else:
        d[i] = -1

print(*d)
