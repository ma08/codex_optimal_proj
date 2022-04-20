

def main():
    n = int(input())
    s = input()
    dp = [0] * (n + 1)
    for i in range(n):
        dp[i + 1] = dp[i] + 1
        if s[i] == 'R' and s[i + 1] == 'L':
            dp[i + 1] = min(dp[i + 1], dp[i] + 1)
    print(dp[n])

if __name__ == '__main__':
    main()
