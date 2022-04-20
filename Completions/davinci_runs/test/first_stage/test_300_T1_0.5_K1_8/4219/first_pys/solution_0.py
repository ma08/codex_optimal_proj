

import sys

n = int(sys.stdin.readline())

testimonies = []
for _ in range(n):
    testimonies.append([])

for i in range(n):
    a_i = int(sys.stdin.readline())
    for _ in range(a_i):
        testimonies[i].append(list(map(int, sys.stdin.readline().split())))

def is_honest(person):
    return 1 if person == "h" else 0

def is_unkind(person):
    return 1 if person == "u" else 0

def solve(n, testimonies):
    # dp[i][j][k] = i番目の人がhonestかunkindかがj, k番目の人がhonestかunkindかがkのときの最大honest人数
    dp = [[[0, 0] for _ in range(n)] for _ in range(n)]
    dp[0][0][0] = 0
    dp[0][0][1] = 1
    dp[0][1][0] = 1
    dp[0][1][1] = 0
    for i in range(n):
        for j in range(2):
            for k in range(2):
                if i == 0:
                    continue
                if j == 0:
                    if k == 0:
                        dp[i][j][k] = dp[i - 1][j][k]
                    else:
                        dp[i][j][k] = max(dp[i - 1][j][k], dp[i - 1][j][0])
                else:
                    if k == 0:
                        dp[i][j][k] = max(dp[i - 1][j][k], dp[i - 1][0][k])
                    else:
                        dp[i][j][k] = max(dp[i - 1][j][k], dp[i - 1][0][k], dp[i - 1][j][0], dp[i - 1][0][0])
    return max(dp[n - 1][0][1], dp[n - 1][1][0], dp[n - 1][1][1])

print(solve(n, testimonies))