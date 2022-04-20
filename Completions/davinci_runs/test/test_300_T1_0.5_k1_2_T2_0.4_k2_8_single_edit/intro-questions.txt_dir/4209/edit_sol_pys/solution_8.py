
import sys

def solve(a):
    n = len(a)
    dp = [1] * n
    for i in range(1, n):
        for j in range(i - 1, -1, -1):
            if a[i] == a[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    return dp

def main():
    n = int(sys.stdin.readline())
    a = list(map(int, sys.stdin.readline().split()))
    dp = solve(a)
    print(max(dp))
    d = max(dp)
    print(d)
    for i in range(n):
        if dp[i] == d:
            print(i - d + 2, i + 1, sep=' ')

if __name__ == '__main__':
    main()
