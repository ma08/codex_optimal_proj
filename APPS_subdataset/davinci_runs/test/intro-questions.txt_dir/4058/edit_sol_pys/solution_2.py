import sys
sys.setrecursionlimit(10**6)

def main():
    n = int(input())
    a = list(map(int, input().split()))
    dp = [0] * n
    dp[0] = 0
    dp[1] = abs(a[1] - a[0])
    for i in range(2, n):
        dp[i] = min(dp[i - 1] + abs(a[i] - a[i - 1]), dp[i - 2] + abs(a[i] - a[i - 2]))
    print(dp[-1])

main()
