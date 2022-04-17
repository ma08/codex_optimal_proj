
import sys

def solve(a, n):
    dp = [1] * (n + 1)
    for i in range(1, n + 1):
        for j in range(i - 1, 0, -1):
            if a[i - 1] == a[j - 1]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)

def main():
    n = int(sys.stdin.readline())
    a = list(map(int, sys.stdin.readline().split()))
    dp = solve(a)
    print(max(dp))
    for i, d in enumerate(dp):
        if d == max(dp):
            print(i - d + 2, i + 1)

if __name__ == '__main__':
    main()
