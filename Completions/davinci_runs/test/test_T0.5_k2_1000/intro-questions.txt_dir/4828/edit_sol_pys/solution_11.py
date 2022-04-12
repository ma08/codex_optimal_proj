

def nop(inp, nop):
    n = len(inp)
    dp = [0] * (n + 1) + [nop + 1]
    for i in range(1, n + 1):
        dp[i] = min(dp[i], dp[i - 1] + 1)
        if inp[i - 1].isupper():
            if i % 4 != 0:
                dp[i] = min(dp[i], dp[i - 1] + (4 - i % 4) + 1)
    return dp[n]

def main():
    inp = list(input())
    print(nop(inp, len(inp) - 1))

if __name__ == '__main__':
    main()
