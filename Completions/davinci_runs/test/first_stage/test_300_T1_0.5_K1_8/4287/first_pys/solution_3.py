

def main():
    a, n, m = map(int, input().split())
    rain = []
    umbrellas = []
    for _ in range(n):
        rain.append(list(map(int, input().split())))
    for _ in range(m):
        umbrellas.append(list(map(int, input().split())))
    umbrellas.sort()
    rain.sort()
    # print(rain)
    # print(umbrellas)

    # dp[i][j] = min fatigue to reach point i with j umbrellas
    # dp[i][j] = min(dp[i-1][j], dp[i-1][j-1] + weight)
    dp = [[float('inf') for _ in range(m+1)] for _ in range(a+1)]
    dp[0][0] = 0
    for i in range(1, a+1):
        for j in range(m+1):
            dp[i][j] = dp[i-1][j]
            if j > 0:
                dp[i][j] = min(dp[i][j], dp[i-1][j-1] + umbrellas[j-1][1])
        for r in rain:
            if r[0] <= i <= r[1]:
                dp[i][0] = float('inf')

    # print(dp)
    if dp[a][0] == float('inf'):
        print(-1)
    else:
        print(dp[a][0])

if __name__ == '__main__':
    main()