

def main():
    a, n, m = map(int, raw_input().split())
    rain = []
    for _ in xrange(n):
        rain.append(map(int, raw_input().split())[1:])
    umbrellas = []
    for _ in xrange(m):
        umbrellas.append(map(int, raw_input().split())[1:])

    # dp[i][j]: minimum fatigue at x=i, using umbrellas up to index j
    dp = [[0] * (m+1) for _ in xrange(a+1)]
    for i in xrange(1, a+1): # x
        for j in xrange(1, m+1): # umbrella index
            if any(map(lambda x: x[0] <= i-1 and i <= x[1], rain)): # raining at i-1
                min_fatigue = float('inf')
                for k in xrange(j): # umbrella index
                    min_fatigue = min(min_fatigue, dp[i-1][k] + umbrellas[k][1])
                dp[i][j] = min_fatigue
            else:
                dp[i][j] = dp[i-1][j]
    print dp[-1][-1]

if __name__ == '__main__':
    main()
