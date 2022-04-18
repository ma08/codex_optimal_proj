
import sys

d, g = list(map(int, sys.stdin.readline().split()))
p_c = []
for _ in range(d):
    p, c = list(map(int, sys.stdin.readline().split()))
    p_c.append((p, c, i))

n = 0
p_c = sorted(p_c, key=lambda x: x[1], reverse=True)
for p, c, i in p_c:
    if g >= c:
        n += p
        g -= c
        break
    else:
        n += p
        g -= p * (i + 1) * 100

if g > 0:
    n += (g + (i + 1) * 100 - 1) // ((i + 1) * 100)

print(n)
