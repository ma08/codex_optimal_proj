

import sys

sys.setrecursionlimit(10 ** 9)


def dfs(i, j, n, m, A, B):
    if i == n or j == m:
        return 0
    res = 0
    if A[i] == B[j]:
        res = dfs(i + 1, j + 1, n, m, A, B) + 1
    else:
        res = max(dfs(i + 1, j, n, m, A, B), dfs(i, j + 1, n, m, A, B))
    return res


def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    print(dfs(0, 0, N, M, A, B))


if __name__ == '__main__':
    main()
