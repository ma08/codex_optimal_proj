

def main():
    n, k = map(int, input().split())
    s = input()
    dp = [0] * (n + 1)  # dp[i] = the max length of the string which can be made from s[:i] or -1 if invalid
    for i in range(1, n + 1):
        for j in range(i):
            if s[j:i] in s:  # if s[j:i] is a substring of s, then it can be used
                dp[i] = max(dp[i], dp[j] + n - i + j)  # dp[j] + n - i + j = len(s[j:i]) + len(s[i:]) or -1 if invalid
    print(dp[n] if dp[n] >= k else -1)

if __name__ == '__main__':
    main()
