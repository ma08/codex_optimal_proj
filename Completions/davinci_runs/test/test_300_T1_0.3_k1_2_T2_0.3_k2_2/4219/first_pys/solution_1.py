

import sys

def main():
    N = int(sys.stdin.readline().rstrip())
    persons = [[] for i in range(N)]
    for i in range(N):
        A_i = int(sys.stdin.readline().rstrip())
        for j in range(A_i):
            x_ij, y_ij = map(int, sys.stdin.readline().rstrip().split())
            persons[i].append((x_ij, y_ij))

    print(solve(N, persons))

def solve(N, persons):
    """
    N: int
    persons: list[list[tuple[int, int]]]
    """
    # dp[i][j] := i番目の人がhonestであるときに、j番目の人がhonestであるときに、
    # それぞれの人の証言が矛盾しないような状態の数
    dp = [[0 for _ in range(2)] for _ in range(N)]
    dp[0][0] = 1
    dp[0][1] = 1
    for i in range(1, N):
        for j in range(2):
            for testimony in persons[i]:
                x_ij, y_ij = testimony
                if j == 1 and y_ij == 1:
                    dp[i][j] += dp[x_ij - 1][1]
                elif j == 0 and y_ij == 0:
                    dp[i][j] += dp[x_ij - 1][0]
    return sum(dp[N - 1])

if __name__ == "__main__":
    main()