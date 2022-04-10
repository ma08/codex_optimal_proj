
import sys

def main():
    n = int(sys.stdin.readline())
    for i in range(n):
        s = sys.stdin.readline().strip()
        print(subsequence(s))


def subsequence(s):
    n = len(s)
    if n == 1:
        return 1
    elif n == 2:
        return 2

    dp = [1] * n
    for i in range(1, n):
        for j in range(i):
            if s[i] > s[j] and dp[i] < dp[j] + 1:
                dp[i] = dp[j] + 1

    return max(dp)


if __name__ == '__main__':
    main()
