



def main():
    a,n,m = map(int,input().split())
    rain = []
    for i in range(n):
        rain.append(list(map(int,input().split())))
    umbrellas = []
    for i in range(m):
        umbrellas.append(list(map(int,input().split())))
    umbrellas.sort()
    rain.sort()
    if rain[0][0] == 0:
        print(-1)
        return
    umbrellas.insert(0,[0,0])
    umbrellas.append([a,0])
    rain.insert(0,[0,0])
    rain.append([a,a])
    dp = [[] for i in range(n+2)]
    dp[0] = [0,0]
    for i in range(1,n+2):
        for j in range(1,m+2):
            if rain[i-1][1] <= umbrellas[j][0]:
                dp[i].append(dp[i-1][j-1])
            else:
                dp[i].append(min(dp[i-1][j-1],dp[i][j-1]+umbrellas[j][1]))
    if dp[n+1][m+1] != dp[n][m+1]:
        print(-1)
        return
    ans = dp[n+1][m+1]
    print(ans)

if __name__ == "__main__":
    main()