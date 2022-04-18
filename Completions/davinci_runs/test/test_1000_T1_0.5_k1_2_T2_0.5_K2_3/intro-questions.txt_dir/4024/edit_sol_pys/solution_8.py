

def main():
    n, k = map(int, input().split())
    s = input()
    dp = [0] * (n + 1) # 初期化
    for i in range(1, n + 1):
        for j in range(i + 1):
            if s[j:i] in s[i:]: # 左から見ていって一致するものがあればそこまでの文字列を追加
                dp[i] = max(dp[i], dp[j] + n - i + j + 1)
    if dp[n] < k:
        print(-1)
    else:
        print(dp[n]) # 文字列の長さ

if __name__ == '__main__':
    main()
