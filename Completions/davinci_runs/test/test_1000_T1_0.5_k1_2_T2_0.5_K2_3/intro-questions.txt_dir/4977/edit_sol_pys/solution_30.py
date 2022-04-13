
import sys, heapq
def main():
    n, m = map(int, sys.stdin.readline().strip().split())
    d = [[0] * n for _ in range(n)]
    for i in range(m):
        a, b, c = map(int, sys.stdin.readline().strip().split())
        a -= 1
        b -= 1
        d[a][b] = c
        d[b][a] = c

    q = []
    heapq.heappush(q, (0, 0))
    dist = [-1] * n
    dist[0] = 0
    while len(q) != 0:
        c, v = heapq.heappop(q)
        for i in range(n):
            if d[v][i] != 0 and (dist[i] == -1 or dist[i] > c + d[v][i]):
                dist[i] = c + d[v][i]
                heapq.heappush(q, (dist[i], i))

    print(dist[n - 1])

if __name__ == '__main__':
    main()
