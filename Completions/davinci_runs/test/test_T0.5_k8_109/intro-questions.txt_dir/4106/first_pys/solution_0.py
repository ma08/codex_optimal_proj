

n, k, x = [int(x) for x in input().split()]
a = [int(x) for x in input().split()]

# if x<k:
#     print(-1)
#     quit()

# if x==k:
#     print(sum(a))
#     quit()

# if x>k:
#     dp = [[0 for i in range(n+1)] for j in range(x+1)]
#     for i in range(n+1):
#         for j in range(x+1):
#             if i==0 or j==0:
#                 dp[i][j]=0
#             elif j<k:
#                 dp[i][j]=dp[i-1][j]
#             else:
#                 dp[i][j]=max(dp[i-1][j], dp[i-1][j-k]+a[i-1])

#     print(dp[n][x])

# print(dp)

if x < k:
    print(-1)
else:
    dp = [0]*(n+1)
    for i in range(1, n+1):
        dp[i] = max(dp[i-1], a[i-1]+dp[max(0, i-k)])
    print(dp[n])