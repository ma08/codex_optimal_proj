

import heapq

def main():
    N,M,X = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(N)]
    C = [int(input()) for _ in range(N)]

    dp = [float("inf")] * (2**M)
    dp[0] = 0
    for i in range(N):
        _dp = dp.copy()
        for j in range(2**M):
            for k in range(M):
                if A[i][k] + (j >> k) % 2 >= X:
                    heapq.heappush(_dp, dp[j] + C[i])
        dp = _dp

    if dp[-1] == float("inf"):
        print(-1)
    else:
        print(dp[-1])


if __name__ == "__main__":
    main()