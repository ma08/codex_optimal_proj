

from sys import stdin

def main():
    code = stdin.readline().strip()
    n = len(code)
    dp = [0] * (n + 1)
    dp[0] = 0
    dp[1] = 0
    dp[2] = 0
    dp[3] = 0
    for i in range(4, n + 1): # i is the length of the substring
        dp[i] = min(dp[i - 1], dp[i - 2], dp[i - 3], dp[i - 4]) + (1 if code[i - 1].isupper() else 0) # 1 if capital, 0 if not
    print(dp[n])

if __name__ == '__main__':
    main()
