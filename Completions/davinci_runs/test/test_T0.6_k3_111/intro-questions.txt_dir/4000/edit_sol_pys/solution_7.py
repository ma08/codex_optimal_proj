

import sys
import math
import heapq
from collections import deque, defaultdict
from itertools import permutations, combinations, product
from operator import itemgetter
from copy import deepcopy
import random

def reverse_int(x):
    y, res = 0, 0
    while x > 0:
        y = x % 10
        res = res * 10 + y
        x /= 10
    return res

def read_list(t): return [t(x) for x in sys.stdin.readline().split()]
def read_line(t): return t(sys.stdin.readline().strip())
def read_lines(t, N): return [t(sys.stdin.readline().strip()) for _ in range(N)]
#

# n = read_line(int)
# adj = defaultdict(list)
# for _ in range(n-1):
#     a, b = read_list(int)
#     adj[a].append(b)
#     adj[b].append(a)
# print adj
n = read_line(int)
adj = defaultdict(list)
for _ in range(n-1):
    a, b = read_list(int)
    adj[a].append(b)
    adj[b].append(a)

def dfs(adj, v, parent, dist):
    for n in adj[v]:
        if n != parent:
            dist[n] = dist[v] + 1
            dfs(adj, n, v, dist)

def find_parent(adj, dist, v):
    maxdist = 0
    maxv = 0
    for n in adj[v]:
        if dist[n] > maxdist:
            maxdist = dist[n]
            maxv = n
    return maxv

def find_max_dist(adj, dist, v):
    q = deque([v])
    while q:
        v = q.popleft()
        if dist[v] == 0:
            continue
        for n in adj[v]:
            if dist[n] == 0:
                q.append(n)
                dist[n] = dist[v] + 1

a = 1
dist = defaultdict(int)
dist[a] = 1
dfs(adj, a, 0, dist)
b = find_parent(adj, dist, a)
dist = defaultdict(int)
dist[b] = 1
dfs(adj, b, 0, dist)
c = find_parent(adj, dist, b)

dist = defaultdict(int)
dist[a] = 1
find_max_dist(adj, dist, a)
dist[b] = 1
find_max_dist(adj, dist, b)
dist[c] = 1
find_max_dist(adj, dist, c)

print max(dist.values())
print a, c, b
