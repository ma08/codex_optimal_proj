

# find the minimum amount of money needed to achieve it.

# 动态规划

# 初始化
# dp[0][0] = 0
# dp[i][0] = +inf
# dp[0][j] = 0

# 状态转移方程
# dp[i][j] = min(dp[i][j], dp[i-1][j-k]+c[i])
# i表示第i本书，j表示满足第j个算法的最小花费
# k表示这本书满足第j个算法的程度，要满足第j个算法，需要对算法j满足的程度大于等于k
# c[i]表示第i本书的花费

# 边界
# dp[i][j] = min(dp[i][j], dp[i-1][j-k]+c[i])
# 对于第i本书，要满足第j个算法，需要对算法j满足的程度大于等于k
# 如果k > j，那么dp[i][j] = +inf

# 结果
# 如果dp[n][m]的值是有限的，那么结果就是dp[n][m]
# 如果dp[n][m]的值是+inf，那么结果就是-1

n, m = map(int, input().split())
c = []
a = []
for i in range(n):
    ci, ai = map(int, input().split())
    c.append(ci)
    a.append(ai)

x = list(map(int, input().split()))

dp = [[float("inf") for i in range(m+1)] for j in range(n+1)]
dp[0][0] = 0
for i in range(n):
    for j in range(m):
        if a[i][j] > 0:
            for k in range(j+1):
                dp[i+1][j] = min(dp[i+1][j], dp[i][j-k]+c[i])

res = dp[n][m]
if res == float("inf"):
    print(-1)
else:
    print(res)