
from collections import deque

n, k = map(int, input().split())
ids = list(map(int, input().split()))

d = deque()

for id in ids:
    if id in d:
        continue
    if len(d) == k:
        d.pop()
    d.appendleft(id)

print(len(d))
print(*d)
