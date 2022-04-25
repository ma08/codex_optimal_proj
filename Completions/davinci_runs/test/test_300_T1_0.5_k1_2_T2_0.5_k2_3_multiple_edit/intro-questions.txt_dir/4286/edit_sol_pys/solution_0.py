import heapq


def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    g = [[] for _ in range(n + 1)]
    for _ in range(m):
        x, y, w = map(int, input().split())
        g[x].append((y, w))
        g[y].append((x, w))

    dist = [float('inf')] * (n + 1)
    dist[1] = 0
    que = []
    heapq.heappush(que, (0, 1))
    while que:
        cost, node = heapq.heappop(que)
        for next_node, next_cost in g[node]:
            if dist[next_node] > cost + next_cost:
                dist[next_node] = cost + next_cost
                heapq.heappush(que, (dist[next_node], next_node))

    ans = sum(a)
    for i in range(2, n + 1):
        ans += min(dist[i], a[i - 1])

    print(ans)


if __name__ == '__main__':
    main()
