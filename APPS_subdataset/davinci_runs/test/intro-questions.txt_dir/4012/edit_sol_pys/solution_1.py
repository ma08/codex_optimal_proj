

# SOLUTION
# We use the fact that the largest number that divides two integers a and b is the greatest common divisor of a and b. 
# Let's denote the greatest common divisor of a and b as gcd(a, b).
# Let's denote the minimum number of operations needed to obtain three integers A <= B <= C such that B is divisible by A and C is divisible by B as f(a, b, c).
# Then f(a, b, c) = min(f(a, b, c-1), f(a, b-1, c-1), f(a, b-1, c)) for a, b, c > 1.
# To obtain the answer, we can use dynamic programming.
# Then dp[a][b][c] = min(dp[a][b][c-1], dp[a][b-1][c-1], dp[a][b-1][c]) for a, b, c > 1.
# The answer is dp[a][b][c].
# The time complexity is O(a*b*c).
# The space complexity is O(a*b*c).

import sys
input = sys.stdin.readline

t = int(input())
while t:
    a, b, c = map(int, input().split())
    dp = [[[0 for _ in range(c+1)] for _ in range(b+1)] for _ in range(a+1)]
    for i in range(1, a+1):
        for j in range(1, b+1):
            for k in range(1, c+1):
                dp[i][j][k] = min(dp[i][j][k-1], dp[i][j-1][k-1], dp[i][j-1][k])
                if i == j == k:
                    dp[i][j][k] = 0
                elif i == j:
                    dp[i][j][k] = dp[i][j][k-1] + 1
                else:
                    dp[i][j][k] = min(dp[i][j][k], dp[i][j-1][k-1] + 1)
                    if j % i == 0:
                        dp[i][j][k] = min(dp[i][j][k], dp[i][j][k-1])
                    else:
                        dp[i][j][k] = min(dp[i][j][k], dp[i][j][k-1] + 1)
    print(dp[a][b][c])
    print(a, b, c)
    t -= 1
