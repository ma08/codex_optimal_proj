
n = int(input())
a = [int(input()) for _ in range(n)]
x = [[0 for _ in range(a[i])] for i in range(n)]
y = [[0 for _ in range(a[i])] for i in range(n)]
for i in range(n):
    for j in range(a[i]):
        x[i][j], y[i][j] = map(int, input().split())
        x[i][j] -= 1

def dfs(i, honest):
    ret = 0
    if honest:
        for j in range(a[i]):
            if y[i][j] == 1:
                ret = max(ret, dfs(x[i][j], 1))
            else:
                ret = max(ret, dfs(x[i][j], 1) + dfs(x[i][j], 0))
    else:
        ret = 1
        for j in range(a[i]):
            if y[i][j] == 1:
                ret = max(ret, dfs(x[i][j], 1) + dfs(x[i][j], 0))
            else:
                ret = max(ret, dfs(x[i][j], 0))
    return ret

ret = 0
for i in range(n):
    ret = max(ret, dfs(i, 1) + dfs(i, 0))
print(ret)
