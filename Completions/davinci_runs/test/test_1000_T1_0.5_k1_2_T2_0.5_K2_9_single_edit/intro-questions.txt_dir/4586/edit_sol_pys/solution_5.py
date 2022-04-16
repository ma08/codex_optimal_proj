import sys
sys.setrecursionlimit(1000000)


n = int(input())
a = [0] * (n + 1)
b = [0] * (n + 1)
c = [0] * (n + 1)
d = [0] * (n + 1)

for i in range(n):
    a[i], b[i], c[i], d[i] = map(int, input().split())


def dfs(i, sum):
    if i == n:
        return sum + d[i]

    res = 0
    for j in range(4):
        if j == 0:
            res = max(res, dfs(i+1, sum + a[i]))
        elif j == 1:
            res = max(res, dfs(i+1, sum + b[i]))
        elif j == 2:
            res = max(res, dfs(i+1, sum + c[i]))
        elif j == 3:
            res = max(res, dfs(i+1, sum + d[i]))
    return res


print(dfs(0, 0))
