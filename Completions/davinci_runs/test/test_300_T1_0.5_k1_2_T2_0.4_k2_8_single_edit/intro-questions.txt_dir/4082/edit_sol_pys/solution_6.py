
def main():
    n = int(input())
    a = list(map(int, input().split()))
    dp1 = [1] * n
    dp2 = [1] * n  # dp1[i] = i番目以降で最大の連続増加数
    for i in range(n - 2, -1, -1):
        if a[i] < a[i + 1]:
            dp1[i] = dp1[i + 1] + 1
    for i in range(1, n):
        if a[i] < a[i - 1]:
            dp2[i] = dp2[i - 1] + 1

    ans = 0
    for i in range(n):
        if i == 0:
            ans = max(ans, dp1[i + 1])
        elif i == n - 1:
            ans = max(ans, dp2[i - 1])
        else:
            ans = max(ans, dp1[i + 1] + dp2[i - 1] - 1)
    print(ans)


if __name__ == "__main__":
    main()
