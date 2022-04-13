
N = int(input())
MOD = 10 ** 9 + 7


dp = [0] * (N+1)
dp[0] = 1


for i in range(N):
    for j in range(10):
        if i + j + 1 > N:
            break
        dp[i+j+1] += dp[i]
        dp[i+j+1] %= MOD
print(dp[-1])
