

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        dp[i] = max(dp[i - 1], a[i - 1])
    ans = sum(dp[i - k] for i in range(k, n + 1))  # 和
    print(ans, end=" ")
    for i in range(n):
        j = i + k
        if j > n: j = n
        while j > i and dp[i] == dp[j]: j -= 1
        print(j - i, end=" ")
        i = j

main()
