

N = int(input())

A = [0] * N
X = [[] for _ in range(N)]
Y = [[] for _ in range(N)]
for i in range(N):
    A[i] = int(input())
    for _ in range(A[i]):
        x, y = map(int, input().split())
        X[i].append(x-1)
        Y[i].append(y)

def is_honest(i, honest):
    for j in range(A[i]):
        if not honest[X[i][j]] and Y[i][j]:
            return False
    return True

def dfs(i, honest):
    if i == N:
        return sum(honest)
    honest[i] = True
    if is_honest(i, honest):
        ret0 = dfs(i+1, honest)
    else:
        ret0 = 0
    honest[i] = False
    if is_honest(i, honest):
        ret1 = dfs(i+1, honest)
    else:
        ret1 = 0
    return max(ret0, ret1)

honest = [False] * N
print(dfs(0, honest))