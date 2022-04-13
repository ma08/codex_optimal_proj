
def num_of_pairs(inp):
    n = len(inp)
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        dp[i] = dp[i - 1]
        if inp[i - 1].isupper():
            if i % 4 != 0:
                dp[i] = min(dp[i], dp[i - 1] + (4 - i % 4))
    return dp[n]

def main():
    inp = list(input())
    print(num_of_pairs(inp))

if __name__ == '__main__':
    main()
