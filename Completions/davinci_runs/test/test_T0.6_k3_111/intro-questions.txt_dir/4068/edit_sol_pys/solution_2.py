
import sys

def main():
    n, m = map(int, input().split())
    a = list(map(int, [input() for _ in range(m)]))
    a.insert(0, 0)
    a.append(n+1)
    a.sort()

    dp = [0]*(n+2)
    dp[0] = 1

    for i in range(1, n+2):
        if i not in a:
            dp[i] = (dp[i-1] + dp[i-2]) % 1_000_000_007

    print(dp[-1])

if __name__ == "__main__":
    main()
