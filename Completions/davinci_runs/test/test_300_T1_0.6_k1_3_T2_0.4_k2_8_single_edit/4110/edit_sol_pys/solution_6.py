
import sys

d, g = list(map(int, sys.stdin.readline().split()))
pc = []
for _ in range(d):
    pc.append(tuple(map(int, sys.stdin.readline().split())))

n = 0
pc = sorted(pc, key=lambda x: x[1], reverse=True)
pc = [(p, c, i) for i, (p, c) in enumerate(pc)]
for p, c, i in pc:
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
