"""
动态规划
dp[i][j]表示总金额为i，硬币种类为j的组合数
"""

A, B, C, X = map(int, input().split())
dp = [[0 for _ in range(C+1)] for _ in range(X+1)]

for i in range(A+1):
    for j in range(B+1):
        for k in range(C+1):
            if i*500+j*100+k*50 <= X:
                if i*500+j*100+k*50 == X:
                    dp[i*500+j*100+k*50][k] += 1
                if i-1 >= 0:
                    dp[i*500+j*100+k*50][k] += dp[(i-1)*500+j*100+k*50][k]
                if j-1 >= 0:
                    dp[i*500+j*100+k*50][k] += dp[i*500+(j-1)*100+k*50][k]
                if k-1 >= 0:
                    dp[i*500+j*100+k*50][k] += dp[i*500+j*100+(k-1)*50][k-1]

print(dp[X][C])
