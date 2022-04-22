
from collections import defaultdict


def dfs(u, p, d):
    for v in graph[u]:
        if v != p and dp[v] == -1:  # not visited
            dfs(v, u, d)
            dp[u] += dp[v] + 1  # add the number of nodes in the subtree


def solve(n, m, d):
    global graph, dp
    graph = defaultdict(list)
    for _ in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    dp = [-1] * (n + 1)
    dfs(1, -1, d)

    if dp[1] != d:
        return "NO"

    ans = ["YES\n"]
    for u in range(1, n + 1):  # loop over all nodes
        for v in graph[u]:  # loop over all neighbors
            if u < v and dp[v] != d:  # check if the subtree is valid
                ans.append(f'{u} {v}')  # add an edge

    return '\n'.join(ans)


def main():
    n, m, d = map(int, input().split())
    print(solve(n, m, d))


if __name__ == '__main__':
    main()
