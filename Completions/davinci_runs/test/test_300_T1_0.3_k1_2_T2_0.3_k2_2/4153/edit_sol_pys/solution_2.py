import sys
sys.setrecursionlimit(10**6)


N, M = map(int, input().split())
A = list(map(int, input().split()))

def dfs(i, s):
    if i == N:
        if s == M:
            print("Yes")
            exit()
        else:
            return

    dfs(i+1, s)
    dfs(i+1, s+A[i])

dfs(0, 0)
print("No")
