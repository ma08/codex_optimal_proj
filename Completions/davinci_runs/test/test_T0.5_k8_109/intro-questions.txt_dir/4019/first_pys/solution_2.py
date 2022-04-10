

import sys
import queue

input = sys.stdin.readline

def solve():
    n, m, D = map(int, input().split())
    edges = [[] for _ in range(n)]
    for _ in range(m):
        v, u = map(int, input().split())
        edges[v - 1].append(u - 1)
        edges[u - 1].append(v - 1)

    if len(edges[0]) > D:
        print('NO')
        return

    q = queue.Queue()
    q.put(0)
    visited = [False] * n
    visited[0] = True
    res = []
    while not q.empty():
        v = q.get()
        for u in edges[v]:
            if not visited[u]:
                visited[u] = True
                q.put(u)
                res.append((v + 1, u + 1))

    if len(res) == n - 1:
        print('YES')
        for v, u in res:
            print(v, u)
    else:
        print('NO')

if __name__ == '__main__':
    solve()