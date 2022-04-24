

from collections import defaultdict
from collections import deque
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort()

d = defaultdict(deque)

for i in range(n):
    for j in range(m):
        d[a[i] + b[j]].append((i, j))

for _ in range(int(input())):
    x = int(input())

    if not d[x]:
        print(-1)
        continue

    i, j = d[x].popleft()
    print(i + 1, j + 1)
