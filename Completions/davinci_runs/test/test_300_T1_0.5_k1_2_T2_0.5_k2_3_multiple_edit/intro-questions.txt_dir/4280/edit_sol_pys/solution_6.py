
n, k = map(int, input().split())

g = [[] for i in range(n)]

g = [[] for i in range(n)]
for i in range(n - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    g[a].append(b)
    g[b].append(a)

dfs(0, -1)
print(k)
for i in range(n - 1):
    print(i % k + 1)
