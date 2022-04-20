

def main():
    n = int(input())
    a = list(map(int, input().split()))  # 入力を受け取る
    dp = [0 for _ in range(n)]
    dp[0] = 1  # 1つ目は必ず1
    for i in range(1, n):
        if a[i] > a[i-1]:
            dp[i] = dp[i-1] + 1  # 連続していれば前の値に1を足す
        else:
            dp[i] = 1
    ans = max(dp)
    for i in range(1, n-1):
        if a[i-1] < a[i+1]:
            ans = max(ans, dp[i-1] + dp[i+1])
    print(ans)

if __name__ == '__main__':
    main()
