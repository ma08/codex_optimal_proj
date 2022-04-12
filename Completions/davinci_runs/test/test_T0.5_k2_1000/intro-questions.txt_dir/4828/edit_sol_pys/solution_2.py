

def nop(inp, k):
    n = len(inp)
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        dp[i] = dp[i - 1] + 1
        if inp[i - 1].isupper():
            if i % k != 0:
                dp[i] = min(dp[i], dp[i - 1] + (k - i % k) + 1)
    return dp[n]

def main():
    inp = list(input())
    k = int(input())
    print(nop(inp, k))

if __name__ == '__main__':
    main()
