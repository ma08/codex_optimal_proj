

from typing import List
from math import log2



def get_contest(problems: List[int]):
    n = len(problems)
    # dp[i][j] = max number of problems in the contest with the maximum difficulty no more than 2^i and the minimum difficulty no less than 2^j
    dp = [[0 for j in range(int(log2(problems[-1])) + 1)] for i in range(int(log2(problems[-1])) + 1)]
    dp[0][0] = 1
    for i in range(n):
        for j in range(int(log2(problems[i])) + 1):
            dp[j][j] += 1
            for k in range(j + 1, int(log2(problems[-1])) + 1):
                dp[k][j] = max(dp[k][j], dp[k - 1][j] + 1)
    return max(map(max, dp))


def main():
    n = int(input())
    problems = list(map(int, input().split()))
    print(get_contest(problems))


if __name__ == '__main__':
    main()
