

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    # dp[i][j] = max profit if we use j days to solve the first i problems
    dp = [[0] * (k+1) for _ in range(n+1)]  # dp[i][j] = max profit if we use j days to solve the first i problems
    for i in range(1, n+1):
        for j in range(1, k+1):
            if j == 1:
                dp[i][j] = sum(a[:i])
            else:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-1] + a[i-1])

    print(dp[n][k])

    # backtrack to find the number of problems for each day
    ans = [0] * k
    i = n
    j = k
    while i > 0:
        if dp[i][j] == dp[i-1][j]:
            i -= 1
        else:
            ans[j-1] += 1
            i -= 1
            j -= 1

    print(*ans)

if __name__ == '__main__':
    main()
