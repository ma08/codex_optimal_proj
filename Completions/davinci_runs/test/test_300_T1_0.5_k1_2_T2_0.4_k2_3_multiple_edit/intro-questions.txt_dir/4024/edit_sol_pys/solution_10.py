
def main():
    n, k = map(int, input().split())
    s = input()
    dp = [0] * (n + 1)  # dp[i] : s[:i] に含まれる文字列の最大の長さ
    for i in range(1, n + 1):
        for j in range(i):
            if s[j:i] in s:  # s[j:i] が s[:i] に含まれているとき
                dp[i] = max(dp[i], dp[j] + n - i + j)  # 長さを更新
    if dp[n] < k:
        print(-1)
    else:
        print(dp[n])

if __name__ == '__main__':
    main()
