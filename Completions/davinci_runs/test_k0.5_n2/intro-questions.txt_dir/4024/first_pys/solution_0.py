

def main():
  n, k = map(int, raw_input().split())
  s = raw_input()

  if k > n:
    print -1
    return

  dp = [[-1 for j in xrange(k)] for i in xrange(n)]
  for i in xrange(n):
    dp[i][0] = n - i

  for i in xrange(1, n):
    for j in xrange(1, k):
      dp[i][j] = dp[i - 1][j]
      for l in xrange(i):
        if s[i] == s[l]:
          dp[i][j] = min(dp[i][j], dp[l][j - 1] + n - i)

  print dp[n - 1][k - 1]

main()