

# Solution by Andrew Xing.

def main():

  n, m, k = [int(x) for x in input().split()]
  grid = [[int(x) for x in input().split()] for i in range(n)]
  
  dp = [[[0 for x in range(k+1)] for y in range(m+1)] for z in range(n+1)]
  dp[1][1][grid[0][0]] = 1
  
  for i in range(1, n+1):
    for j in range(1, m+1):
      if i == 1 and j == 1:
        continue
      for x in range(k+1):
        if i > 1:
          dp[i][j][x^grid[i-1][j-1]] += dp[i-1][j][x]
        if j > 1:
          dp[i][j][x^grid[i-1][j-1]] += dp[i][j-1][x]
  
  print(dp[n][m][k])

if __name__ == "__main__":
  main()
