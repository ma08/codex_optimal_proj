
import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
a = [[] for _ in range(n+1)]
visited = [False] * (n+1)

n, k = map(int, sys.stdin.readline().split())
p = list(map(int, sys.stdin.readline().split()))

print(sum(sorted(p)[:k]))
