

def main():
    n, a, b, k = map(int, input().split())
    h = list(map(int, input().split()))
    dp = [0] * (k + 1)
    for i in range(n):
        for j in range(k + 1):
            if j == 0:
                dp[j] = dp[j] + (h[i] - 1) // a
            else:
                dp[j] = dp[j] + (h[i] - 1) // a + (h[i] - 1) // b
                if i > 0:
                    dp[j] = max(dp[j], dp[j - 1] + (h[i] - b) // a)
    print(dp[k])

main()
