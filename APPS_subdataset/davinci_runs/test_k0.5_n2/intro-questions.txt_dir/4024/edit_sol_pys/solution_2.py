

def main():
  n, k = map(int, input().split())
  s = input()

  if k > n:
    print -1
    return

  dp = [[-1 for j in range(k)] for i in range(n)]
  for i in xrange(n):
    dp[i][0] = n - i

  for i in range(1, n):
    for j in range(1, k):
      dp[i][j] = dp[i - 1][j]
      for l in range(i):
        if s[i] == s[l]:
          dp[i][j] = min(dp[i][j], dp[l][j - 1] + n - i)

  print dp[n - 1][k - 1]

main()
