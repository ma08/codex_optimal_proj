
def get_fatigue(x, rain, umbrellas):
    if any(map(lambda r: r[0] <= x-1 and x <= r[1], rain)): # raining at i-1
        min_fatigue = float('inf')
        for k in xrange(1, len(umbrellas)+1):
            min_fatigue = min(min_fatigue, dp[x-1][k] + umbrellas[k-1][1])
        return min_fatigue
    else:
        return dp[x-1][len(umbrellas)]

def main():
    a, n, m = map(int, raw_input().split())
    rain = []
    for _ in xrange(n):
        rain.append(map(int, raw_input().split()))
    umbrellas = []
    for _ in xrange(m):
        umbrellas.append(map(int, raw_input().split()))

    # dp[i][j]: minimum fatigue at x=i, using umbrellas up to index j
    dp = [[0] * (m+1) for _ in xrange(a+1)]
    for i in xrange(1, a+1):
        for j in xrange(m+1):
            dp[i][j] = get_fatigue(i, rain, umbrellas[:j])
    print dp[-1][-1]

if __name__ == '__main__':
    main()
