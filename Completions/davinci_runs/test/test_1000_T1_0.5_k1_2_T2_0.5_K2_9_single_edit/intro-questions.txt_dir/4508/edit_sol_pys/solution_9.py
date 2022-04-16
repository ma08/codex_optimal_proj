
import sys
import math
from collections import defaultdict

def add_edge(adj, u, v):
    adj[u].append(v)
    adj[v].append(u)

def dfs(adj, u, par):
    for v in adj[u]:
        if v != par:
            dfs(adj, v, u)

def solve(adj, n):
    dfs(adj, 1, 0)
    count = 0
    for u in adj:
        if len(adj[u]) == 1:
            count += 1
    if count == 2:
        return 0
    else:
        return math.ceil((count - 2)/2)

def main():
    n = int(input())
    adj = defaultdict(list)
    for _ in range(n - 1):
        u, v = [int(i) for i in input().split()]
        add_edge(adj, u, v)
    print(solve(adj, n))

if __name__ == '__main__':
    main()
