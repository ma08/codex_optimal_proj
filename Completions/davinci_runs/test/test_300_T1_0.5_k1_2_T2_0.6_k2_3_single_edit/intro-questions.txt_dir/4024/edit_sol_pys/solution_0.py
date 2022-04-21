

def main():
    n, k = map(int, input().split())
    s = input()
    dp = [0] * (n + 1) # 初期化
    for i in range(1, n + 1):
        for j in range(i):
            if s[j:i] in s: # s[j:i]がsの中にあるかどうか
                dp[i] = max(dp[i], dp[j] + n - i + j) # dp[i]の最大値を記録
    if dp[n] < k:
        print(-1)
    else:
        print(dp[n])

if __name__ == '__main__':
    main()
