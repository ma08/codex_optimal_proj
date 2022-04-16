import sys
sys.setrecursionlimit(10 ** 7)

def dfs(v, p):
    for u in tree[v]:
        if u == p:
            continue
        dfs(u, v)
        d[v] += d[u]

def dfs2(v, p, x):
    for u in tree[v]:
        if u == p:
            continue
        dfs2(u, v, x + d[v] - d[u])
    ans[v] = x


def main():
    global d, tree, ans
    n = int(input())
    tree = [[] for _ in range(n)]
    for _ in range(n - 1):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        tree[a].append(b)
        tree[b].append(a)
    d = [0] * n
    dfs(0, -1)
    ans = [0] * n
    dfs2(0, -1, 0)
    print(*ans, sep='\n')

if __name__ == '__main__':
    main()
