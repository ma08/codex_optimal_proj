
def main():
    n = int(input())
    a = list(map(int, input().split()))
    dp_inc = [1] * n
    dp_dec = [1] * n
    for i in range(1, n):
        if a[i] > a[i - 1]:
            dp_inc[i] = dp_inc[i - 1] + 1
        if a[n - i - 1] > a[n - i]:
            dp_dec[n - i - 1] = dp_dec[n - i] + 1

    ans = 0
    for i in range(n):
        if i == 0:
            ans = max(ans, dp_inc[i + 1])
        elif i == n - 1:
            ans = max(ans, dp_dec[i - 1])
        else:
            ans = max(ans, dp_inc[i + 1] + dp_dec[i - 1] - 1)
    print(ans)


if __name__ == "__main__":
    main()
