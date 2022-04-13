

from sys import stdin, stdout, stderr

def main():
    for line in stdin:
        line = list(map(int, line.strip().split('+')))
        n = len(line)
        dp = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            dp[i][i] = 1
            if i > 0 and line[i] == line[i-1]*10 + line[i]: # 1+1+1
                dp[i-1][i] = 1
            if i > 1 and line[i] == line[i-2]*100 + line[i-1]*10 + line[i]: # 1+11+1
                dp[i-2][i] = 1
        for i in range(n-1):
            for j in range(i+2, n):
                dp[i][j] = dp[i][j-1] + dp[i+1][j] - dp[i+1][j-1]
                if line[j] == line[j-1]*10 + line[j]: # 1+1
                    dp[i][j] += 1
        stdout.write(str(dp[0][-1]) + '\n')

main()
