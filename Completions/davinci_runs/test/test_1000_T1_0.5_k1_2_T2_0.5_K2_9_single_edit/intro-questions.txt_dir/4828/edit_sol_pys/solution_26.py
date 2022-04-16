

def nop(inp):
    n = len(inp)
    dp = [float('inf')] * (n + 1)
    dp[0] = 0
    for i in range(1, n + 1):
        if inp[i - 1].isupper():
            dp[i] = min(dp[i], dp[i - 1] + (4 - i % 4))
        dp[i] = min(dp[i], dp[i - 1] + 1)
    return dp[n]

def main():
    inp = list(input())
    print(nop(inp))

if __name__ == '__main__':
    main()
