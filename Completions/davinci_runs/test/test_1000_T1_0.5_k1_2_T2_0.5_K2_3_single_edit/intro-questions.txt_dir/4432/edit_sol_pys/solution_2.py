
import sys

def main():
    t = int(sys.stdin.readline())
    for _ in range(t):
        n = int(sys.stdin.readline())
        a = list(map(int, sys.stdin.readline().strip().split()))
        assert n == len(a)
        dp = [0] * n
        dp[0] = a[0]
        for i in range(1, n):
            dp[i] = max(dp[i-1] + a[i], a[i], dp[i-2] + a[i])
        print(max(dp))

if __name__ == '__main__':
    main()
