

import heapq


def solve(N, M, X, C, A):
    # dp[i][j]: the minimum cost to achieve the goal when we have already read the first i books and the understanding level of the j-th algorithm is x
    dp = [[float('inf')] * (M + 1) for _ in range(N + 1)]
    dp[0][0] = 0
    for i in range(1, N + 1):
        for j in range(M + 1):
            if j + A[i - 1] <= M:
                dp[j + A[i - 1]][i] = min(dp[j + A[i - 1]][i], dp[j][i - 1] + C[i - 1])
            dp[j][i] = min(dp[j][i], dp[j][i - 1])
    if dp[M][N] == float('inf'):
        return -1
    return dp[M][N]


def main():
    N, M, X = map(int, input().split())
    C = [0] * N
    A = [0] * N
    for i in range(N):
        C[i], *A[i] = map(int, input().split())[1:]
    print(solve(N, M, X, C, A))


def test():
    assert solve(3, 2, 10, [10, 2, 5], [[3, 2], [4, 1], [1, 4]]) == 7
    assert solve(4, 3, 10, [6, 2, 3, 5], [[4, 2, 3], [3, 3, 2], [2, 3, 4], [4, 2, 1]]) == -1
    assert solve(3, 4, 10, [5, 4, 3], [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]]) == 12
    assert solve(1, 1, 10, [100], [[10]]) == 100


if __name__ == "__main__":
    test()
    main()
