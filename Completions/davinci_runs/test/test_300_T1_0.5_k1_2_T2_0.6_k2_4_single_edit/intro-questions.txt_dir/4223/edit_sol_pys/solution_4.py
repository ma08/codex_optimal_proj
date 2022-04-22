

from collections import Counter, deque

N = int(input())
A = list(map(int, input().split()))

cnt = Counter(A)
cnt_k = cnt.keys()
cnt_v = cnt.values()

ans = n - sum(c.values())

print(ans)
