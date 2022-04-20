
from collections import deque

n = int(input())
a = list(map(int, input().split()))

q = deque([a[0]])
for i in range(1, n):
    if a[i] <= 2 * q[0]:
        q[0] = a[i]
    else:
        q.appendleft(a[i])

print(len(q))
