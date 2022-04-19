

N, M = map(int, input().split())
A = list(map(int, input().split()))

A.sort()

def dfs(i, s):
    if i == N:
        return s == M
    if dfs(i+1, s):
        return True
    if dfs(i+1, s+A[i]):
        return True
    return False

if dfs(0, 0):
    print("Yes")
else:
    print("No")
