

def main():
    """
    The idea is to use dynamic programming to calculate subproblems.
    For each character in the string, find the minimum cost to create a set of size k.
    """
    n, k = map(int, input().split())
    s = input()
    dp = [0] * (k + 1)
    for i in range(n):
        for j in range(k, 0, -1):
            if j == 1:
                dp[j] = dp[j] + 1
            else:
                dp[j] = min(dp[j], dp[j - 1])
    result = dp[k]
    print(result if result <= n else -1)

if __name__ == '__main__':
    main()