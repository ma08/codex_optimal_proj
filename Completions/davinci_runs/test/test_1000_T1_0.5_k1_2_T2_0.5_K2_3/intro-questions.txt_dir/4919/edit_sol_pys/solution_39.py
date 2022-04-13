
from collections import defaultdict

n = int(raw_input())
trips = defaultdict(list)

for _ in range(n):
    c, y = input().split()
    trips[c].append(int(y))

q = int(raw_input())

for _ in range(q):
    c, k = input().split()
    print(trips[c][int(k) - 1])
