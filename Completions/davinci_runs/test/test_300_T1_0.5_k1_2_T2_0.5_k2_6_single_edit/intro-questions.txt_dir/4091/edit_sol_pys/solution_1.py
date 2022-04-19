

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    dp = [0]*(n+1)
    for i in range(1, n+1):
        dp[i] = max(dp[i-1], a[i-1])
    ans = 0
    for i in range(k, n+1):
        ans += dp[i-k]  # dp[i-k] is the maximum value of the k numbers before i
    print(ans)
    i = 0
    while i < n:
        j = min(i+k, n)  # j is the index of the first number after i that is not equal to dp[i]
        while j > i and dp[i] == dp[j]:
            j -= 1
        print(j-i,end=" ")
        i = j
    print()

main()
