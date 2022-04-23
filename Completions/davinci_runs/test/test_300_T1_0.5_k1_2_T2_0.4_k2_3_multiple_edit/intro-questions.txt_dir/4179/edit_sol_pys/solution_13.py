
import sys

def main():
    n, k = map(int, sys.stdin.readline().split())
    h = list(map(int, sys.stdin.readline().split()))
    h.sort()
    dp = [float("inf")] * (n + 1)
    dp[0] = 0
    for i in range(n):
        for j in range(1, k + 1):
            if i + j < n:
                dp[i + j] = min(dp[i + j], dp[i] + abs(h[i + j] - h[i]))
            else:
                break
    print(dp[-1])

if __name__ == "__main__":
    main()
