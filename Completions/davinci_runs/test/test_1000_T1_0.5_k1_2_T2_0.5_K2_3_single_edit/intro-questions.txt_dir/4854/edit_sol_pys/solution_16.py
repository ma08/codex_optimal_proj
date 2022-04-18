


#!/usr/bin/env python3

n, c = map(int, input().split())
msg = list(map(int, input().split()))

count = [0] * (c + 1)
for m in msg:
    count[m] += 1

res = []
for i in range(c + 1):
    res += [i] * count[i]

print(' '.join(map(str, res)))
