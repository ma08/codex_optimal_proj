

N, M = map(int, input().split())
A = list(map(int, input().split()))

# N, M = 3, 3
# A = [2, 3, 5]

def dfs(i, m):
    if m == 0:
        return 1
    if i >= N:
        return 0
    res = dfs(i + 1, m) or dfs(i + 1, m - A[i])
    return res

def solve():
    if dfs(0, M):
        print('Yes')
    else:
        print('No')

solve()
