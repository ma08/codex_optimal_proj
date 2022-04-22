
import sys

def solve(a):
    n = len(a)
    dp = [1] * n
    for i in range(1, n):
        for j in range(i):
            if a[i] >= a[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    return dp

def main():
    n = int(sys.stdin.readline())
    a = list(map(int, sys.stdin.readline().split()))
    dp = solve(a)
    print(max(dp) - 1)
    for i, d in enumerate(dp):
        if d == max(dp) and d > 1:
            print(i + 1, end=' ')
    print('')

if __name__ == '__main__':
    main()
