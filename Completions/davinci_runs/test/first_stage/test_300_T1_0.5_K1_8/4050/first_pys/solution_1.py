

def solve(a):
    n = len(a)
    sums = [0] * n
    sums[0] = a[0]
    for i in range(1, n):
        sums[i] = sums[i-1] + a[i]

    dp = [0] * n
    for i in range(n):
        dp[i] = [0] * n

    for i in range(n):
        dp[i][i] = 1

    for i in range(n-1):
        if a[i] == a[i+1]:
            dp[i][i+1] = 1

    for i in range(n):
        for j in range(i+2, n):
            if sums[j] - sums[i] == a[i] * (j-i+1):
                dp[i][j] = 1

    for i in range(n):
        for j in range(i+2, n):
            for k in range(i, j):
                if dp[i][k] == 1 and dp[k+1][j] == 1:
                    dp[i][j] = 1
                    break

    for i in range(n):
        for j in range(n):
            if dp[i][j] == 1:
                print(i+1, j+1)

n = int(input())
a = list(map(int, input().split()))
solve(a)