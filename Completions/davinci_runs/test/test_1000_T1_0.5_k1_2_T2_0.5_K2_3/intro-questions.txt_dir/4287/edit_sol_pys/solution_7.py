

def main():
    a, n, m = map(int, input().split())
    rain = []
    for _ in range(n):
        rain.append(map(int, input().split()))
    umbrellas = []
    for _ in range(m):
        umbrellas.append(map(int, input().split()))

    # dp[i][j]: minimum fatigue at x=i, using umbrellas up to index j
    dp = [[0] * (m+1) for _ in range(a+1)]
    for i in range(1, a+1):
        for j in range(m+1):
            if any(map(lambda x: x[0] <= i-1 and i <= x[1], rain)): # raining at i-1
                min_fatigue = float('inf')
                for k in range(1, j+1):
                    min_fatigue = min(min_fatigue, dp[i-1][k] + umbrellas[k-1][1])
                dp[i][j] = min_fatigue
            else:
                dp[i][j] = dp[i-1][j]
    print dp[-1][-1]

if __name__ == '__main__':
    main()
