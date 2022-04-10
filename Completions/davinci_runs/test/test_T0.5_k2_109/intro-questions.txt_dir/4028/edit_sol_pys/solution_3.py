
n = int(input())
s = input()

dp = [0] * (n+1)
dp[0] = 1

for i in range(1, n+1):
    for j in range(i):
        if (j == 0) or (j > 0 and s[2*j-1:2*j+1] == "()"):  # j == 0 or j > 0 and s[2*j-1:2*j+1] == "()"
            dp[i] += 2 * dp[j]

print(dp[n] % 1000000007)
