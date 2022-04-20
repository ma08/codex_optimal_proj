

def main():
    n = int(input())
    dp = [0]*(n+1)
    dp[1] = 10
    mod = 10**9 + 7
    for i in range(2,n+1):
        dp[i] = dp[i-1]*9 + dp[i-2]*10
        dp[i] %= mod
    print(dp[n])

if __name__ == '__main__':
    main()