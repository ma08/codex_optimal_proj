

def main():
    n, k = map(int, input().split())
    s = input()
    dp = [0] * (n + 1)  # dp[i] = the max length of the string which can be made from s[:i] + s[i:]
    for i in range(1, n + 1):
        for j in range(i):
            if s[j:i] in s:  # if s[j:i] is a substring of s
                dp[i] = max(dp[i], dp[j] + n - i + j)  # dp[j] + n - i + j = len(s[j:i]) + len(s[i:]) = len(s[j:])
    if dp[n] < k:
        print(-1)
    else:
        print(dp[n])

if __name__ == '__main__':
    main()
