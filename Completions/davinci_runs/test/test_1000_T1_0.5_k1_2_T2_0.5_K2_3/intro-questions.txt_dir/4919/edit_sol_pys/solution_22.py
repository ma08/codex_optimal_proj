#input
from collections import defaultdict
import sys

n = int(sys.stdin.readline())
trips = defaultdict(list)

for _ in range(n):
    c, y = sys.stdin.readline().split()
    trips[c].append(int(y))

q = int(sys.stdin.readline())

for _ in range(q):
    c, k = sys.stdin.readline().split()
    print(trips[c][int(k) - 1])
