

from collections import defaultdict

n = int(input())
trips = defaultdict(lambda: [])

for _ in range(n):
    c, y = input().split()[0]
    trips[c].append(y)

q = int(input())

for _ in range(q):
    c, k = input().split()
    k = int(k)
    if k <= len(trips[c]):
        print(trips[c][k - 1])
    else:
        print(-1)
