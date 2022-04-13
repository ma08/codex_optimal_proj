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
    for i, c in enumerate(dp):
        if c == max(dp):
            print(i - c + 2, i + 1, end=' ')

if __name__ == '__main__':
    main()
