

N, M = map(int, input().split())
A = [int(x) for x in input().split()]

def dfs(i, m, s):
    if m == 0:
        return s

    if i >= N:
        return -1

    res = dfs(i+1, m, s)
    if res != -1:
        return res

    res = dfs(i+1, m-1, s+A[i])
    return res

if dfs(0, M, 0) == -1:
    print('No')
else:
    print('Yes')
