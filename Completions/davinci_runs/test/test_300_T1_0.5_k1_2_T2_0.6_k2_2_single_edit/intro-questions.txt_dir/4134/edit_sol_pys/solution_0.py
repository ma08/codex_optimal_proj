
# Solution by Andrew Xing

def main():

  n, m, k = [int(x) for x in input().split()]
  grid = [[int(x) for x in input().split()] for i in range(n)]
  
  dp = [[[0 for x in range(k+1)] for y in range(m+1)] for z in range(n+1)]
  dp[1][1][grid[0][0]] = 1
  
  for y in range(1, n+1):
    for x in range(1, m+1):
      if y == 1 and x == 1:
        continue
      for z in range(k+1):
        if y > 1:
          dp[y][x][z^grid[y-1][x-1]] += dp[y-1][x][z]
        if x > 1:
          dp[y][x][z^grid[y-1][x-1]] += dp[y][x-1][z]
  
  print(dp[n][m][k] % 1000000007)

if __name__ == "__main__":
  main()
