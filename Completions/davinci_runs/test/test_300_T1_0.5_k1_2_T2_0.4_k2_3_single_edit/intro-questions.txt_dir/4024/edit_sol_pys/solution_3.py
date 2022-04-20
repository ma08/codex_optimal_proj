import sys
sys.setrecursionlimit(10 ** 7)

def main():
    n = int(input())
    a = list(map(int, input().split()))
    dp = [0] * n
    for i in range(n):
        dp[i] = max(dp[i - 1] + a[i], a[i])
    print(max(dp))

if __name__ == '__main__':
    main()
