


def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    ans = 0
    for i in range(n):
        if i == 0:
            if a[i] + 1 != a[i + 1]:
                ans += a[i + 1] - a[i] - 1
        elif i == n - 1:
            if a[i] - 1 != a[i - 1]:
                ans += a[i] - a[i - 1] - 1
        else:
            if a[i] + 1 != a[i + 1] and a[i] - 1 != a[i - 1]:
                ans += min(a[i + 1] - a[i] - 1, a[i] - a[i - 1] - 1)
    print(ans)


if __name__ == "__main__":
    main()
