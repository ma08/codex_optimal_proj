

import sys
import math
from collections import defaultdict

sys.setrecursionlimit(10 ** 6)

n = int(input())
a = list(map(int, input().split()))

edges = []
for _ in range(n - 1):
    u, v = map(int, input().split())
    edges.append((u - 1, v - 1))

adj = defaultdict(list)
for u, v in edges:
    adj[u].append(v)
    adj[v].append(u)

def dfs(u, p):
    subtree_size_u = 1
    subtree_sum_u = a[u]
    for v in adj[u]:
        if v != p:
            subtree_size_v, subtree_sum_v = dfs(v, u)
            subtree_size_u += subtree_size_v
            subtree_sum_u += subtree_sum_v
    return subtree_size_u, subtree_sum_u

def solve(u, p):
    subtree_size_u = 1
    subtree_sum_u = a[u]
    for v in adj[u]:
        if v != p:
            subtree_size_v, subtree_sum_v = dfs(v, u)
            subtree_size_u += subtree_size_v
            subtree_sum_u += subtree_sum_v
    max_cost = subtree_sum_u
    for v in adj[u]:
        if v != p:
            max_cost = max(max_cost, solve(v, u) + subtree_sum_u - subtree_sum_v)
    return max_cost


print(solve(0, -1))
