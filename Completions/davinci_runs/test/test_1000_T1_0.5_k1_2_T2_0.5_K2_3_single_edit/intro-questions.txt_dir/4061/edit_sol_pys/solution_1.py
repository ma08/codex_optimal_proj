
import sys

def main():
    s = sys.stdin.readline().strip()
    t = sys.stdin.readline().strip()
    n = len(s)
    dp = [0] * n
    for i in range(n):
        if s[i] in t:
            if i == 0:
                dp[i] = 0
            else:
                dp[i] = dp[i - 1]
        else:
            if i == 0:
                dp[i] = 1
            else:
                dp[i] = dp[i - 1] + 1
    print(max(dp))

if __name__ == "__main__":
    main()
