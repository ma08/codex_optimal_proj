import sys

n, x = map(int, input().split())
l = list(map(int, input().split()))

# 初期値
count = 1
d = 0

if n == 1:
    if l[0] <= x:
        count = 2
    else:
        count = 1
else:
    for i in range(n):
        d += l[i]
        if d <= x:
            count += 1

print(count)
