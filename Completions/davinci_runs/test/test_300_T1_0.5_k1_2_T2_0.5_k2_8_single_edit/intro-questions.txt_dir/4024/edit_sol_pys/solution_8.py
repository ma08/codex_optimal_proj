

def main():
    n, k = map(int, input().split())
    s = input()
    dp = [0] * (n + 1) #记录字符串长度
    for i in range(1, n + 1):
        for j in range(i):
            if s[j:i] in s: #如果子串在s中出现过
                dp[i] = max(dp[i], dp[j] + n - i + j)
    if dp[n] < k: #如果最大长度小于k
        print(-1)
    else:
        print(dp[n])

if __name__ == '__main__':
    main()
