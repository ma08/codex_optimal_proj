

def main():
    n = int(input())
    s = input()
    dp = [[0 for _ in range(n*2+1)] for _ in range(n*2+1)]
    dp[0][0] = 1
    for i in range(1,n*2+1):
        for j in range(i+1):
            if j>0:
                dp[i][j] += dp[i-1][j-1]
            if j<i:
                dp[i][j] += dp[i-1][j+1]
    count = 0
    for i in range(len(s)+1):
        if i==0:
            count += dp[n*2][0]
        elif i==len(s):
            count += dp[n*2][n*2]
        else:
            count += dp[n*2-i][n*2-i-len(s)+1]
    print(count%(10**9+7))

main()