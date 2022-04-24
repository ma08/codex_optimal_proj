import math


def solve(n, a):
    dp = [0] * n
    dp[0] = 1
    for i in range(1, n):
        if a[i] > a[i - 1]:
            dp[i] = dp[i - 1] + 1
        else:
            dp[i] = dp[i - 1]
    return dp[n - 1]

def main():
    n = int(input())
    a = [int(x) for x in input().split()]
    ans = solve(n, a)
    print(ans)

if __name__ == '__main__':
    main()
