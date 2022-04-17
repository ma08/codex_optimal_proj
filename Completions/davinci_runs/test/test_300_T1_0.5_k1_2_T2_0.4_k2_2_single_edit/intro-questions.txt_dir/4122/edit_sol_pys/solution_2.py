
import sys
# Solution

H, n = map(int, input().split())
d = list(map(int, input().split()))

hp = H
minute = 0

for i in range(n):
    hp += d[i]
    minute += 1
    if hp <= 0:
        sys.stdout.write(str(minute))
        break
else:
    sys.stdout.write(str(-1))
