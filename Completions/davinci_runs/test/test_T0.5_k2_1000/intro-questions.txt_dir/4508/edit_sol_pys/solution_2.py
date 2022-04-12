
import sys
import math
from collections import defaultdict

sys.setrecursionlimit(10**6)

def read_list():
    return [int(x) for x in input().split()]

def read_single_int():
    return int(read_single_str())

def read_single_str():
    return sys.stdin.readline().rstrip()

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
    for u in range(1, n + 1):
        if len(adj[u]) == 1 and u != 1:
            count += 1
    return math.ceil((count - 2)/2)

def main():
    n = read_single_int()
    adj = defaultdict(list)
    for _ in range(n - 1):
        u, v = read_list()
        add_edge(adj, u, v)
    print(solve(adj, n))

if __name__ == '__main__':
    main()
