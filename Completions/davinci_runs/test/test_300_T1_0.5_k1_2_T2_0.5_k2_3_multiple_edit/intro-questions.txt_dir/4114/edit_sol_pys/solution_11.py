import sys
sys.setrecursionlimit(10**6)

def dfs(v):
    visited[v] = True
    for next_v in graph[v]:
        if not visited[next_v]:
            dfs(next_v)
    postorder.append(v)

def main():
    n, m = map(int, sys.stdin.readline().rstrip().split())
    graph = [[] for _ in range(n)]
    for i in range(m):
        a, b = map(int, sys.stdin.readline().rstrip().split())
        graph[a - 1].append(b - 1)
    visited = [False] * n
    postorder = []
    for i in range(n):
        if not visited[i]:
            dfs(i)
    print(*postorder[::-1])

if __name__ == "__main__":
    main()
