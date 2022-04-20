

import sys, heapq

def main():
    n, m, k = [int(x) for x in sys.stdin.readline().split()]
    roads = [[int(x) for x in sys.stdin.readline().split()] for _ in range(m+1)]
    print(n, m, k)
    print(roads)
    # dijkstra
    dist = [float('inf')] * (n+1)
    dist[1] = 0
    pq = []
    heapq.heappush(pq, (0, 1))
    while pq:
        d, node = heapq.heappop(pq)
        if dist[node] < d:
            continue
        for road in roads[node]:
            if dist[road[0]] > dist[node] + road[1]:
                dist[road[0]] = dist[node] + road[1]
                heapq.heappush(pq, (dist[road[0]], road[0]))

    print(dist)


if __name__ == "__main__":
    main()
