

def main():
    a, n, m = map(int, raw_input().split())
    rain = []
    for _ in xrange(n):
        rain.append(list(map(int, raw_input().split())))
    umbrellas = []
    for _ in xrange(m):
        umbrellas.append(list(map(int, raw_input().split())))

    # dp[i][j]: minimum fatigue at x=i, using umbrellas up to index j
    dp = [[0] * (m+1) for _ in xrange(a+1)]
    for i in xrange(1, a+1):
        for j in xrange(m+1):
            if any(map(lambda x: x[0] <= i-1 and i <= x[1], rain)): # raining at i-1
                min_fatigue = float('inf')
                for k in xrange(1, j+1):
                    min_fatigue = min(min_fatigue, dp[i-1][k] + umbrellas[k-1][1])
                dp[i][j] = min_fatigue
            else:
                dp[i][j] = dp[i-1][j]
    print dp[-1][-1]

if __name__ == '__main__':
    main()
