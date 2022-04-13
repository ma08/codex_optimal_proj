# -*- coding: utf-8 -*-

import sys
from collections import defaultdict, deque


def solve(n, m, s):
    adj_list = defaultdict(list)
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        adj_list[u].append(v)
    visited = [False] * (n + 1)
    queue = deque()
    queue.append(s)
    visited[s] = True
    while len(queue):
        v = queue.popleft()
        for u in adj_list[v]:
            if not visited[u]:
                queue.append(u)
                visited[u] = True
    count = 0
    for v in range(1, n + 1):
        if not visited[v]:
            count += 1
    return count

def main():
    n, m, s = map(int, sys.stdin.readline().split())
    print solve(n, m, s)

if __name__ == '__main__':
    main()
