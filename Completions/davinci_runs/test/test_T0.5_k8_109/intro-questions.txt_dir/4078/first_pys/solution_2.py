
import sys
import math

def main():
  n, m = map(int, raw_input().split())
  a = map(int, raw_input().split())
  segs = []
  for i in xrange(m):
    l, r = map(int, raw_input().split())
    segs.append((l, r, i+1))
  segs.sort()
  segs = [(l, r, i) for (l, r, i) in segs if l <= r]
  dp = [[0] * (m + 1) for i in xrange(n + 1)]
  for i in xrange(1, n + 1):
    for j in xrange(1, m + 1):
      dp[i][j] = dp[i][j - 1]
      for seg in segs:
        l, r, k = seg
        if l <= i <= r:
          dp[i][j] = max(dp[i][j], dp[l - 1][j - 1] + (a[i - 1] - a[l - 1]))
  #print dp
  sol = dp[n][m]
  #print sol
  print sol
  if sol == 0:
    print 0
    return
  ans = []
  i = n
  j = m
  while i > 0 and j > 0:
    if dp[i][j] == dp[i][j - 1]:
      j -= 1
    else:
      for seg in segs:
        l, r, k = seg
        if l <= i <= r:
          if dp[i][j] == dp[l - 1][j - 1] + (a[i - 1] - a[l - 1]):
            ans.append(k)
            i = l - 1
            j -= 1
            break
  ans.reverse()
  print len(ans)
  print " ".join(map(str, ans))

if __name__ == "__main__":
  main()