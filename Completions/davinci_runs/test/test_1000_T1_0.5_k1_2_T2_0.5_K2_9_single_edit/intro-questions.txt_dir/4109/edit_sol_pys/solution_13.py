
import sys
sys.setrecursionlimit(10 ** 7)


def solve(N, M, X, C, A):
    # dp[i][j]: the minimum cost to achieve the goal when we have already read the first i books and the understanding level of the j-th algorithm is x.
    dp = [[float('inf')] * (M + 1) for _ in range(N + 1)]
    dp[0][0] = 0 # dp[0][0] = 0 means that we have not read any book and the understanding level of the j-th algorithm is 0.
    for i in range(1, N + 1): # for each book
        for j in range(M + 1): # for each understanding level
            dp[i][j] = dp[i - 1][j] # do not read the ith book
            if j + A[i - 1] <= M: # if reading the ith book does not exceed the maximum level
                dp[i][j + A[i - 1]] = min(dp[i][j + A[i - 1]], dp[i - 1][j] + C[i - 1]) # read the ith book
    if dp[N][M] == float('inf'): # if we cannot reach the maximum level
        return -1 # return -1
    return dp[N][M] # return the minimum cost


def main():
    N, M, X = map(int, input().split())
    C = [0] * N
    A = [[0] * M for _ in range(N)]
    for i in range(N):
        C[i], *A[i] = map(int, input().split())
    print(solve(N, M, X, C, A))


def test():
    assert solve(3, 2, 10, [10, 2, 5], [[3, 2], [4, 1], [1, 4]]) == 7
    assert solve(4, 3, 10, [6, 2, 3, 5], [[4, 2, 3], [3, 3, 2], [2, 3, 4], [4, 2, 1]]) == -1
    assert solve(3, 4, 10, [5, 4, 3], [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]]) == 12
    assert solve(1, 1, 10, [100], [[10]]) == 100


if __name__ == "__main__":
    test()
    main()
