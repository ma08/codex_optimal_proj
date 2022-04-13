import sys


def main():
    n = int(sys.stdin.readline())
    a = list(map(int, sys.stdin.readline().split()))
    dp = [0] * n
    for i in range(n):
        for j in range(i):
            if a[i] > a[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    print(max(dp) + 1)


if __name__ == "__main__":
    main()
