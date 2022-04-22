
from itertools import permutations
import sys

N, A, B, C = list(map(int, sys.stdin.readline().split()))
l = []
for i in range(N):
    l.append(int(sys.stdin.readline()))

ans = float('inf')
for p in permutations([i for i in range(N)]):
    a = 0
    b = 0
    c = 0
    mp = 100
    for i in range(N):
        if p[i] == 0:
            a += l[i]
        elif p[i] == 1:
            b += l[i]
        elif p[i] == 2:
            c += l[i]
        else:
            mp -= 10
    if a == A and b == B and c == C:
        ans = min(ans, mp)

print(ans)
