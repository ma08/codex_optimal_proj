

# SOLUTION

#!/usr/bin/env python3

n = int(input())
a = list(map(int, input().split()))

d = [0] * n

for i in range(n - 1, -1, -1):
    if i + a[i] < n:
        d[i] = d[i + a[i]] + 1
    if i - a[i] >= 0:
        d[i] = min(d[i], d[i - a[i]] + 1)
    if d[i] == 0:
        d[i] = -1



# SOLUTION

#!/usr/bin/env python3

n = int(input())
a = list(map(int, input().split()))

d = [0] * n

for i in range(n - 1, -1, -1):
    if i + a[i] < n:
        d[i] = d[i + a[i]] + 1
    if i - a[i] >= 0:
        d[i] = min(d[i], d[i - a[i]] + 1)
    if d[i] == 0:
        d[i] = -1

print(*d)
print(*d)
