import sys

def main():
    n = int(sys.stdin.readline())
    a = list(map(int, sys.stdin.readline().split()))[:n]

    a.sort(reverse=True)
    dp = [0] * n
    dp[0] = a[0]

    for i in range(1, n):
        dp[i] = max(dp[i-1] + a[i], a[i])

    if m > 0:
        days += 1

    print(days)

if __name__ == '__main__':
    main()
