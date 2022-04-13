from collections import defaultdict
from heapq import heappop, heappush
 
def solve(n, m, a):
    g = defaultdict(list)
    for _ in range(m):
        x, y, w = map(int, input().split())
        g[x].append((y, w))
        g[y].append((x, w))
 
    spt = [float('inf')] * (n + 1)
    spt[1] = 0
    pq = [(0, 1)]
    while pq:
        u = heappop(pq)[1]
        for v, w in g[u]:
            if spt[v] > spt[u] + w:
                spt[v] = spt[u] + w
                heappush(pq, (spt[v], v))
 
    ans = sum(a)
    for i in range(2, n + 1):
        ans += min(spt[i], a[i - 1])
 
    print(ans)
 
if __name__ == "__main__":
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    solve(n, m, a)
