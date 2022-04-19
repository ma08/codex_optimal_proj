

import sys
# Solution

H, n = map(int, sys.stdin.readline().split())
d = list(map(int, sys.stdin.readline().split()))

hp = H
minute = 0

for i in range(n):
    hp += d[i]
    minute += 1
    if hp <= 0:
        print(minute, end='')
        break
else:
    print(-1, end='')
