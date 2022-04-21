

from itertools import accumulate

N, H, L, R = map(int, input().split())
A = list(map(int, input().split()))

t = [0] + list(accumulate(A))
t = [i % H for i in t]

c = 0
for i in range(N):
    if L <= t[i+1] <= R:
        c += 1
print(c)
