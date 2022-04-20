


def main():  
  n, m, k = [int(x) for x in input().split()]
  grid = [[int(x) for x in input().split()] for i in range(n)]  
  dp = [[[0 for x in range(k+1)] for y in range(m+1)] for z in range(n+1)]
  dp[0][0][grid[0][0]] = 1  
  for i in range(n):
    for j in range(m):
      for x in range(k+1):
        if i > 0:
          dp[i][j][x^grid[i][j]] += dp[i-1][j][x]
        if j > 0:
          dp[i][j][x^grid[i][j]] += dp[i][j-1][x]
  print(dp[n-1][m-1][k])

if __name__ == "__main__":  
  main()
