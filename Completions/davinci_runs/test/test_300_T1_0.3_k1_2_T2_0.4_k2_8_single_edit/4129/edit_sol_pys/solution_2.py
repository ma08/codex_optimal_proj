
#
import sys

def main():
    n, m, s = map(int, sys.stdin.readline().split())
    adj = [[] for _ in range(n+1)]
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        adj[u].append(v)
    visited = [False] * (n+1)
    stack = [s]
    while stack:
        u = stack.pop()
        if not visited[u]:
            visited[u] = True
            for v in adj[u]:
                stack.append(v)
    print(sum(1 for i in range(1, n+1) if not visited[i]))

if __name__ == '__main__':
    main()
