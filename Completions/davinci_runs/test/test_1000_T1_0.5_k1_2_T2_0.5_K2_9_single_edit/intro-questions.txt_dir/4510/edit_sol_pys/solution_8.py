
from collections import deque

n, k = map(int, input().split())
ids = deque(map(int, input().split()))

d = []

for id in ids:
    if id not in d:
        d.append(id)
    if len(d) == k:
        d.pop(0)

print(len(d))
print(*d, sep=' ')
