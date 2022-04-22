

from collections import Counter

from functools import partial

N, K = map(int, input().split())

A = Counter()
for i in range(K):
    d = int(input())
    A.update(list(map(int, input().split())))

ans = N - len(A.keys())
print(ans)
