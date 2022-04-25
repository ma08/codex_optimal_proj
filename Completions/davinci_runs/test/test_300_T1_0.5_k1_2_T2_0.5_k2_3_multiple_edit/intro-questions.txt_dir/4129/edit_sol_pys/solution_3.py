import sys, os

def main():
    n, m, s = map(int, sys.stdin.readline().strip().split())
    roads = []
    for i in range(m):
        a, b = map(int, sys.stdin.readline().strip().split())
        roads.append((a, b))

    # Graph
    graph = [[] for i in range(n+1)]
    for (a, b) in roads:
        graph[a].append(b)

    # DFS
    visited = [False for i in range(n+1)]
    stack = [s]
    while stack:
        a = stack.pop()
        visited[a] = True
        for b in graph[a]:
            if not visited[b]:
                stack.append(b)

    # Count
    res = 0
    for i in range(1, n+1):
        if i == s:
            continue
        if not visited[i]:
            res += 1

    print(res)


if __name__ == '__main__':
    main()
