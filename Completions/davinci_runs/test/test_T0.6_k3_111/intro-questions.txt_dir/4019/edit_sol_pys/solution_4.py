
import sys
import math
from collections import defaultdict
from heapq import heapify, heappush, heappop

def main():
    n, m, D = map(int, sys.stdin.readline().split())
    graph = defaultdict(list)
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        graph[u].append(v)
        graph[v].append(u)
    
    if D >= n - 1:
        print("YES")
        for i in range(1, n):
            print(1, i)
        return
    
    if n - 1 == m:
        print("NO")
        return
        
    visited = [True] + [False] * (n - 1)
    parent = [0] * n
    Q = [(0, 1)]
    heapify(Q)
    
    while Q:
        d, u = heappop(Q)
        visited[u] = True
        
        for v in graph[u]:
            if not visited[v]:
                heappush(Q, (d + 1, v))
                parent[v] = u
    
    if D == 1:
        print("YES")
        for i in range(2, n):
            print(1, i)
        return
    
    if D == n - 1:
        print("YES")
        for i in range(2, n):
            print(i, parent[i])
        return
    
    print("YES")
    for i in range(2, D + 1):
        print(1, i)
    for i in range(D + 1, n):
        print(i, parent[i])

if __name__ == "__main__":
    main()
