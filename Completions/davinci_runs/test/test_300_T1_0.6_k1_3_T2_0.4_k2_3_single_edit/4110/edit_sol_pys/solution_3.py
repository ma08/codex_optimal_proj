
import sys

N = int(input())
A = list(map(int, input().split()))

n = 0
p_c = sorted(p_c, key=lambda x: x[1], reverse=True)
p_c = [(p, c, i) for i, (p, c) in enumerate(p_c)]
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
