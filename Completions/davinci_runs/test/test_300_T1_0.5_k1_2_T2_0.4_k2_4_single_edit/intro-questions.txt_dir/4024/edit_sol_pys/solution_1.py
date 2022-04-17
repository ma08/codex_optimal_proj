import sys
sys.setrecursionlimit(10 ** 7)

def main():
    n = int(input())
    s = input()
    if s[0] == '0':
        print(0)
        return
    dp = [0] * n
    dp[0] = 1
    for i in range(1, n):
        if s[i] == '0':
            if s[i - 1] == '1' or s[i - 1] == '2':
                dp[i] = dp[i - 1]
            else:
                print(0)
                return
        else:
            if s[i - 1] == '0':
                dp[i] = dp[i - 1]
            elif int(s[i - 1:i + 1]) <= 26:
                dp[i] = dp[i - 1] + dp[i - 2]
            else:
                dp[i] = dp[i - 1]
    print(dp[-1] % (10 ** 9 + 7))

if __name__ == '__main__':
    main()
