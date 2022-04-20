

def main():
    N, M, S = map(int, input().split())
    g = [[] for _ in range(N)]
    for _ in range(M):
        u, v = map(int, input().split())
        g[u-1].append(v-1)
    S -= 1
    visited = [0]*N
    stack = [S]
    while stack:
        u = stack.pop()
        visited[u] = 1
        for v in g[u]:
            if not visited[v]:
                stack.append(v)
    print(N-1-sum(visited))

main()