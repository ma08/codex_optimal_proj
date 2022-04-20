

import heapq


def solve(N, M, X, C, A):
    # dp[i]: the minimum cost to achieve the goal when we have already read the first i books
    dp = [float('inf')] * (N + 1)
    dp[0] = 0
    for i in range(1, N + 1):  # for each book
        new_dp = [float('inf')] * (N + 1)
        for j in range(M + 1):  # for each understanding level
            if j + A[i - 1] <= M:  # if we can read the book
                new_dp[j + A[i - 1]] = min(new_dp[j + A[i - 1]], dp[j] + C[i - 1])
            new_dp[j] = min(new_dp[j], dp[j])
        dp = new_dp
    if dp[M] == float('inf'):
        return -1
    return dp[M]


def main():
    N, M, X = map(int, input().split())
    C = [0] * N
    A = [0] * N
    for i in range(N):
        C[i], A[i] = map(int, input().split())
    print(solve(N, M, X, C, A))


def test():
    assert solve(3, 2, 10, [10, 2, 5], [[3, 2], [4, 1], [1, 4]]) == 7
    assert solve(4, 3, 10, [6, 2, 3, 5], [[4, 2, 3], [3, 3, 2], [2, 3, 4], [4, 2, 1]]) == -1
    assert solve(3, 4, 10, [5, 4, 3], [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]]) == 12
    assert solve(1, 1, 10, [100], [[10]]) == 100


if __name__ == "__main__":
    test()
    main()
