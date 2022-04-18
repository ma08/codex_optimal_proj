

def nops(inp):
    n = len(inp)
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        dp[i] = dp[i - 1]
        if inp[i - 1].isupper():
            dp[i] = min(dp[i], dp[i - 1] + (4 - i % 4) if i % 4 != 0 else 0)
    return dp[n]

def main():
    inp = list(input())
    print(nops(inp))

if __name__ == '__main__':
    main()
