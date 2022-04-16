import heapq


def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    g = [[] for _ in range(n + 1)]
    for _ in range(m):
        x, y, w = map(int, input().split())
        g[x].append((y, w))
        g[y].append((x, w))

    spt = [float('inf')] * (n + 1)
    spt[1] = 0
    q = [(0, 1)]
    heapq.heapify(q)
    while q:
        u = heapq.heappop(q)
        for v, w in g[u]:
            if spt[v] > spt[u] + w:
                spt[v] = spt[u] + w
                heapq.heappush(q, (spt[v], v))

    ans = sum(a)
    for i in range(2, n + 1):
        ans += min(spt[i], a[i - 1])

    print(ans)


if __name__ == '__main__':
    main()
