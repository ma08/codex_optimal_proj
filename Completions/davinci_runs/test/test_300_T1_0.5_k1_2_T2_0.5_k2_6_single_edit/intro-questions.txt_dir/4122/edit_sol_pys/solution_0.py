
# Solution

import sys

input = sys.stdin.readline
n = int(input())

for i in range(n):
    hp += d[i]
    minute += 1
    if hp <= 0:
        print(minute)
        break
else:
    print(-1)
