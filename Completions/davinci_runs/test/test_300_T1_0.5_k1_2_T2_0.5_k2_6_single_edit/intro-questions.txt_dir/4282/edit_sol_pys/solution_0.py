

from collections import defaultdict, deque

def solve(n, m, a):
    d = defaultdict(list)
    for i in range(m):
        u, v = map(int, input().split())
        d[u].append(v)
        d[v].append(u)
    visited = [False] * (n + 1)
    q = deque()
    q.append(1)
    visited[1] = True
    res = 0
    while q:
        for i in range(len(q)):
            u = q.popleft()
            for v in d[u]:
                if not visited[v]:
                    q.append(v)
                    visited[v] = True
        res += 1
    return res - 1

n = int(input())
m = int(input())
print(solve(n, m, []))
