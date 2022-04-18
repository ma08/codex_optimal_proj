

def main():
    n = int(input())
    a = list(map(int, input().split()))
    dp = [0] * n
    for i in range(n):
        if i == 0:
            dp[i] = a[i]
        else:
            dp[i] = dp[i-1] + a[i]
    q = int(input())
    for _ in range(q):
        l, r = map(int, input().split())
        if l == 1:
            print(dp[r-1])
        else:
            print(dp[r-1] - dp[l-2])

if __name__ == '__main__':
    main()
