

def main():
    s = input()
    t = input()
    s_len = len(s)
    t_len = len(t)
    dp = [0] * (s_len + 1)
    for i in range(t_len):
        dp[i] = i
    for i in range(t_len, s_len):
        dp[i] = t_len
    for i in range(t_len - 1, -1, -1):
        for j in range(s_len - 1, -1, -1):
            if s[j] == t[i]:
                dp[j] = min(dp[j], dp[j + 1] + 1)
    print(s_len - dp[0])

if __name__ == '__main__':
    main()