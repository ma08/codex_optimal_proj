

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    dp = [a[0]]
    for i in range(1, n):  # i = 1 to n-1
        if a[i] > dp[-1]:
            dp.append(a[i])
        else:
            for j in range(len(dp)):
                if dp[j] >= a[i]:
                    dp[j] = a[i]
                    break
    print(len(dp))
    print(*dp)

solve()
