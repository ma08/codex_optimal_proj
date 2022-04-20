

# Solution by Andrew Xing, edited by Andrew Xing

def main():

  n, m, k = [int(x) for x in input().split()] # n rows, m columns, k target
  grid = [[int(x) for x in input().split()] for i in range(n)] # grid
  
  dp = [[[0 for x in range(k+1)] for y in range(m+1)] for z in range(n+1)] # dp table
  dp[1][1][grid[0][0]] = 1 # base case
  
  for i in range(1, n+1):
    for j in range(1, m+1):
      if i == 1 and j == 1: # base case
        continue
      for x in range(k+1):
        if i > 1: # if not on first row
          dp[i][j][x^grid[i-1][j-1]] += dp[i-1][j][x] # add number of ways to get to previous cell
        if j > 1: # if not on first column
          dp[i][j][x^grid[i-1][j-1]] += dp[i][j-1][x] # add number of ways to get to previous cell
  
  print(dp[n][m][k]) # number of ways to get to bottom right cell with target k

if __name__ == "__main__":
  main()
