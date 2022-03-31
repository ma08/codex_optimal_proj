

import sys

def main():
    n = int(sys.stdin.readline())
    a = [int(i) for i in sys.stdin.readline().split()]
    dp = [1] * n
    for i in range(n):
        for j in range(i):
            if a[j] < a[i] and dp[i] < dp[j] + 1:
                dp[i] = dp[j] + 1
    print(max(dp))

if __name__ == "__main__":
    main()