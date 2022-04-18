def main(): 
    N = int(input())
    mod = 10 ** 9 + 7 
    dp = [0] * (N + 1) 
    dp[1] = 10 
    # dp[i] = dp[i-1] * 9 + dp[i-2] * 10 
    for i in range(2, N + 1): 
        dp[i] = dp[i - 1] * 9 + dp[i - 2] * 10 
        dp[i] %= mod 
    print(dp[N]) 
if __name__ == "__main__": 
    main() 
