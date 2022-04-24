
# SOLUTION

def commonChild(s1, s2):
    n = len(s1)
    m = len(s2)

    dp = [[0 for i in range(m + 1)] for i in range(n + 1)]

    for i in range(n):
        for j in range(m):
            if s1[i] == s2[j]:
                dp[i + 1][j + 1] = 1 + dp[i][j]
            else:
                dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j])
    return dp[n][m]

if len(d) == 1:
  print(1)
  quit()

l = list(d.values())

res = 1

for i in l:
  res *= (i + 1)

res -= 1

print(res)
