
from sys import stdin, stdout

def main():
    for line in stdin:
        line = list(map(int, line.strip().split('+')))
        n = len(line)
        dp = [[0 for _ in range(n)] for _ in range(n)] # dp[i][j] means the number of expressions that sum up to line[i:j+1]
        for i in range(n):
            dp[i][i] = 1
            if i > 0:
                dp[i-1][i] = 2
        for i in range(n-1):
            for j in range(i+2, n):
                dp[i][j] = dp[i][j-1] + dp[i+1][j] - dp[i+1][j-1]
                if line[j] == line[j-1]*10 + line[j]:
                    dp[i][j] += 1
        stdout.write(str(dp[0][-1]) + '\n')

main()
