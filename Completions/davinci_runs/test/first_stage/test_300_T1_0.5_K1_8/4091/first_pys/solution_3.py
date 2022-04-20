

def main():
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    dp = [[0 for _ in range(n+1)] for _ in range(k+1)]
    for i in range(1,n+1):
        dp[1][i] = sum(a[:i])
    for i in range(2,k+1):
        for j in range(i,n+1):
            dp[i][j] = max(dp[i][j-1],dp[i-1][j-1]+a[j-1])
    for i in range(k,0,-1):
        for j in range(n,0,-1):
            if dp[i][j] != dp[i][j-1]:
                print(j-1,end=' ')
                break
    print()
    print(dp[k][n])

if __name__ == '__main__':
    main()