



def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    dp = [0 for i in range(200001)]
    for i in range(n):
        dp[a[i]] += 1
    for i in range(1, 200001):
        dp[i] += dp[i-1]
    ans = []
    for i in range(k):
        if dp[a[n-i-1]] - dp[a[n-i-1]-1] > 0:
            ans.append(a[n-i-1])
            dp[a[n-i-1]] -= 1
        else:
            j = n-i-1
            while j >= 0 and dp[a[j]] - dp[a[j]-1] == 0:
                j -= 1
            ans.append(a[j])
            dp[a[j]] -= 1
    print(*ans)


if __name__ == "__main__":
    main()