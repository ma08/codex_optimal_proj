
import sys

x = int(input())
s = sys.stdin.readline().strip()

w = 0
m = 0
i = 0

for c in s:
    if c == 'W':
        w += 1
    else:
        m += 1
    if abs(w - m) > x:
        break
    i += 1

print(i)
