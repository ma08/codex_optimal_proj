

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    dp = [0]*(n+1)  # dp[i] := a[i]からa[n]までの最大値
    for i in range(1, n+1):
        dp[i] = max(dp[i-1], a[i-1])  # dp[i] = max(dp[i-1], a[i-1])
    ans = 0
    for i in range(k, n+1):
        ans += dp[i - k]  # dp[i]からa[i-k]までの最大値を足す
    print(ans)
    i = 0
    while i < n:
        j = i + k
        if j > n:
            j = n
        while j > i and dp[i] == dp[j]:  # 同じ値を持つ場合は距離を短くする
            j -= 1
        print(j - i, end=" ")
        i = j
    print()

main()
