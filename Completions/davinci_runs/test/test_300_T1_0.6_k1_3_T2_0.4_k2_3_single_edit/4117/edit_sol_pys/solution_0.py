import sys
sys.setrecursionlimit(10**6)

def main():
    n, k = map(int, input().split())
    h = list(map(int, input().split()))
    dp = [float('inf')] * n
    dp[0] = 0
    for i in range(1, n):
        for j in range(1, k+1):
            if i - j >= 0:
                dp[i] = min(dp[i], dp[i-j]+abs(h[i]-h[i-j]))
    print(dp[-1])

if __name__ == '__main__':
    main()
