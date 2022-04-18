

# Solution by Andrew Xing

def main():

  n, m, k = [int(x) for x in input().split()]
  grid = [[int(x) for x in input().split()] for i in range(n)]
  
  dp = [[[0 for x in range(k+1)] for y in range(m+1)] for z in range(n+1)] # dp[i][j][x] is number of ways to get to (i,j) with xor of path being x
  dp[1][1][grid[0][0]] = 1
  
  for i in range(1, n+1): # i is row
    for j in range(1, m+1): # j is column
      if i == 1 and j == 1:
        continue
      for x in range(k+1): # x is xor of path
        if i > 1:
          dp[i][j][x^grid[i-1][j-1]] += dp[i-1][j][x] # add number of ways to get to (i-1, j) with xor of path being x
        if j > 1:
          dp[i][j][x^grid[i-1][j-1]] += dp[i][j-1][x] # add number of ways to get to (i, j-1) with xor of path being x
  
  print(dp[n][m][k])

if __name__ == "__main__":
  main()
