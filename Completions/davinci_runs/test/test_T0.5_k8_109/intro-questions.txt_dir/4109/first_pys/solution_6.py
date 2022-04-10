

# https://atcoder.jp/contests/abc161/tasks/abc161_f

# input
N, M = map(int, input().split())
A = []
for i in range(N):
    A.append(list(map(int, input().split())))
C = list(map(int, input().split()))

# 全探索

def dfs(i, X):
    if i == N:
        if sum(X) >= M:
            return 0
        else:
            return 1e9
    res0 = dfs(i+1, X)
    X_next = [max(X[j], A[i][j]) for j in range(M)]
    res1 = dfs(i+1, X_next) + C[i]
    return min(res0, res1)

X = [0]*M
print(dfs(0, X))