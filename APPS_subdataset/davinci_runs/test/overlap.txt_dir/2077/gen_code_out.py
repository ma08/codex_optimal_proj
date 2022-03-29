

import sys

def main():
    n, m = map(int, sys.stdin.readline().split())
    graph = [[] for _ in range(n)]
    for _ in range(m):
        a, b = map(int, sys.stdin.readline().split())
        graph[a - 1].append(b - 1)
        graph[b - 1].append(a - 1)
    topics = list(map(int, sys.stdin.readline().split()))
    topics = [t - 1 for t in topics]
    order = [-1] * n
    for i in range(n):
        if order[topics[i]] != -1:
            print(-1)
            return
        order[topics[i]] = i
    for i in range(n):
        if order[i] == -1:
            order[i] = n
    order = [o + 1 for o in order]
    print(*order)

if __name__ == '__main__':
    main()