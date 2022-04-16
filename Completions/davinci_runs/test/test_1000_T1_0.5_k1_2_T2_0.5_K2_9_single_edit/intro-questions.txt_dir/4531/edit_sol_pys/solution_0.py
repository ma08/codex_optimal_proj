

import sys
import math
from collections import defaultdict, deque

sys.setrecursionlimit(10 ** 7)

n = int(input())

adj = defaultdict(list)
a = list(map(int, input().split()))

edges = []
for _ in range(n - 1):
    u, v = map(int, input().split())
    edges.append((u - 1, v - 1))
            subtree_sum_list += [subtree_sum_list[-1] + a[v] for _ in range(subtree_size_v)]
    return subtree_size, subtree_sum, subtree_sum_list


def solve(u, p):
    subtree_size, subtree_sum, subtree_sum_list = dfs(u, p)
    max_cost = subtree_sum
    for v in adj[u]:
        if v != p:
            subtree_size_v, subtree_sum_v, subtree_sum_list_v = dfs(v, u)
            max_cost = max(max_cost, solve(v, u) + subtree_sum - subtree_sum_v)
            max_cost = max(max_cost, solve(v, u) + subtree_sum - subtree_sum_v)
            max_cost = max(max_cost, solve(v, u) + subtree_sum - subtree_sum_v)
            max_cost = max(max_cost, solve(v, u) + subtree_sum - subtree_sum_v)
            max_cost = max(max_cost, solve(v, u) + subtree_sum - subtree_sum_v)
            max_cost = max(max_cost, solve(v, u) + subtree_sum - subtree_sum_v)
            max_cost = max(max_cost, solve(v, u) + subtree_sum - subtree_sum_v)
            max_cost = max(max_cost, solve(v, u) + subtree_sum - subtree_sum_v)
            max_cost = max(max_cost, solve(v, u) + subtree_sum - subtree_sum_v)
            max_cost = max(max_cost, solve(v, u) + subtree_sum - subtree_sum_v)
            max_cost = max(max_cost, solve(v, u) + subtree_sum - subtree_sum_v)
            max_cost = max(max_cost, solve(v, u) + subtree_sum - subtree_sum_v)
            max_cost = max(max_cost, solve(v, u) + subtree_sum - subtree_sum_v)
            max_cost = max(max_cost, solve(v, u) + subtree_sum - subtree_sum_v)
            max_cost = max(max_cost, solve(v, u) + subtree_sum - subtree_sum_v)
            max_cost = max(max_cost, solve(v, u) + subtree_sum - subtree_sum_v)
            max_cost = max(max_cost, solve(v, u) + subtree_sum - subtree_sum_v)
            max_cost = max(max_cost, solve(v, u) + subtree_sum - subtree_sum_v)
            max_cost = max(max_cost, solve(v, u) + subtree_sum - subtree_sum_v)
            max_cost = max(max_cost, solve(v, u) + subtree_sum - subtree_sum_v)
            max_cost = max(max_cost, solve(v, u) + subtree_sum - subtree_sum_v)
            max_cost = max(max_cost, solve(v, u) + subtree_sum - subtree_sum_v)
            max_cost = max(max_cost, solve(v, u) + subtree_sum - subtree_sum_v)
            max_cost = max(max_cost, solve(v, u) + subtree_sum - subtree_sum_v)
            max_cost = max(max_cost, solve(v, u) + subtree_sum - subtree_sum_v)
            max_cost = max(max_cost, solve(v, u) + subtree_sum - subtree_sum_v)
            max_cost = max(max_cost, solve(v, u) + subtree_sum - subtree_sum_v)
            max_cost = max(max_cost, solve(v, u) + subtree_sum - subtree_sum_v)
            max_cost = max(max_cost, solve(v, u) + subtree_sum - subtree_sum_v)
            max_cost = max(max_cost, solve(v, u) + subtree_sum - subtree_sum_v)
            max_cost = max(max_cost, solve(v, u) + subtree_sum - subtree_sum_v)
            max_cost = max(max_cost, solve(v, u) + subtree_sum - subtree_sum_v)
            max_cost = max(max_cost, solve(v, u) + subtree_sum - subtree_sum_v)
            max_cost = max(max_cost, solve(v, u) + subtree_sum - subtree_sum_v)
            max_cost = max(max_cost, solve(v, u) + subtree_sum - subtree_sum_v)
            max_cost = max(max_cost, solve(v, u) + subtree_sum - subtree_sum_v)

for u, v in edges:
    adj[u].append(v)
    adj[v].append(u)


def dfs(u, p):
    subtree_sum_list = [a[u]]
    subtree_size = 1
    subtree_sum = a[u]
    for v in adj[u]:
        if v != p:
            subtree_size_v, subtree_sum_v, subtree_sum_list_v = dfs(v, u)
            subtree_sum_list += subtree_sum_list_v
            subtree_size += subtree_size_v
            subtree_sum += subtree_sum_v
    return subtree_size, subtree_sum


print(solve(0, -1))
