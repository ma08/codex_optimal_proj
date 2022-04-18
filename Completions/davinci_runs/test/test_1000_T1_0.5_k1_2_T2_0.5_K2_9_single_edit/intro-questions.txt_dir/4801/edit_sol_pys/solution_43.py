
def solve():
    n = int(input())
    a = list(map(int, input().split()))
    dp = [a[0], a[1]]
    for i in range(1, n):
        if a[i] >= dp[-1]:
            dp.append(a[i])
        else:
            dp[bisect.bisect_left(dp, a[i])] = a[i]
    print(len(dp))
    print(*dp)

solve()
