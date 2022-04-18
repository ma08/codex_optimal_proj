N, M = map(int, input().split())
A = [int(input()) for i in range(M)]


def dfs(n, m, A, num):
    if n == N:
        if m == M:
            return num
        else:
            return -1
    else:
        if m == M:
            return -1

        if n == 0:
            if A[m] == 0:
                return -1
            else:
                return dfs(n+1, m+1, A, str(A[m]))
        else:
            if A[m] == 0:
                return dfs(n+1, m, A, num+"0")
            else:
                return dfs(n+1, m+1, A, num+str(A[m]))

print(dfs(0, 0, A, ""))
