

def main():
    """
    The idea is to use dynamic programming to calculate sub problems.
    For each character in the string, find the minimum cost to create a set of size k. 
    """
    n, k = map(int, input().split())
    s = input()
    dp = [0] * (k + 1) # dp[i] is the minimum cost to create a set of size i
    for i in range(n):
        for j in range(k, 0, -1):
            if j == 1:
                dp[j] = dp[j] + 1 # if we have a set of size 1, then the cost is the number of characters we have seen so far
            else:
                dp[j] = min(dp[j], dp[j - 1]) # the cost is the minimum of the cost of the previous set or the cost of the current set
    result = dp[k]
    print(result if result <= n else -1)

if __name__ == '__main__':
    main()
