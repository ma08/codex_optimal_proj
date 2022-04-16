

n, m, q = map(int, input().split())
A = []
for i in range(m):
    A.append(list(map(int, input().split())))
B = []
for i in range(q):
    B.append(list(map(int, input().split())))


def dfs(i, a):
    if i == n:
        return
    for j in range(a, m):
        dfs(i+1, j)


dfs(0, 0)
