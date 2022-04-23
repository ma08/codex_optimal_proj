
def main():
    n = int(input())
    a = list(map(int, input().split()))
    dp = [1] * n
    dp_2 = [1] * n
    for i in range(1, n):  # これは前からやる
        if a[i] > a[i - 1]:
            dp[i] = dp[i - 1] + 1
    for i in range(1, n):  # これは後ろからやる
        if a[n - i - 1] > a[n - i]:  # 後ろからやるときは i - 1 ではなく n - i - 1
            dp_2[n - i - 1] = dp_2[n - i] + 1

    ans = 0
    for i in range(n):
        if i == 0:
            ans = max(ans, dp[i + 1])
        elif i == n - 1:
            ans = max(ans, dp_2[i - 1])
        else:
            ans = max(ans, dp[i + 1] + dp_2[i - 1] - 1)
    print(ans)


if __name__ == "__main__":
    main()
