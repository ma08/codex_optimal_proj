

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))
    d = list(map(int, input().split()))
    e = list(map(int, input().split()))

    # print(a)
    # print(b)
    # print(c)
    # print(d)
    # print(e)

    dp = [[[0]*n for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                dp[i][j][k] = a[i]*b[j]*c[k] + dp[i-1][j][k]

    for j in range(n):
        for k in range(n):
            for i in range(n):
                dp[i][j][k] = a[i]*b[j]*c[k] + dp[i][j-1][k]

    for k in range(n):
        for i in range(n):
            for j in range(n):
                dp[i][j][k] = a[i]*b[j]*c[k] + dp[i][j][k-1]

    print(dp[n-1][n-1][n-1])

if __name__ == "__main__":
    main()
