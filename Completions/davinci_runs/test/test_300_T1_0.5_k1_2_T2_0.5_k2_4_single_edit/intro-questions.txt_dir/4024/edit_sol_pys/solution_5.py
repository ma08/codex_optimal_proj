

def main():
    n, k = map(int, input().split())
    s = input()
    dp = [0] * (n + 1) # 初期化
        if dp[i] >= k:
            print(i)
            return
    for i in range(1, n + 1):
        for j in range(i):
            if s[j:i] == s[j:i][::-1]:
                dp[i] = max(dp[i], dp[j] + i - j)

if __name__ == '__main__':
    main()
