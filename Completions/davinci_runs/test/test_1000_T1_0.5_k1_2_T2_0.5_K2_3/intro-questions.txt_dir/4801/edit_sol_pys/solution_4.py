

def solve():
    n = int(input())
    ai = list(map(int, input().split()))
    dp = [ai[0]]
    for i in range(1, n):
        if ai[i] > dp[-1]:
            dp.append(ai[i])
        else:
            for j in range(len(dp)):
                if dp[j] >= ai[i]:
                    dp[j] = ai[i]
                    break
    print(len(dp))
    print(*dp, sep=" ")

solve()
