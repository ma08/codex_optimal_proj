


def main():
    n, h, l, r = map(int, input().split())
    a = list(map(int, input().split()))

    for i in range(n):
        if a[i] > h:
            a[i] -= h

    ans = 0
    for i in range(n):
        if l <= a[i] <= r:
            ans += 1
        if i + 1 < n:
            if (l <= a[i] <= r) and (l <= a[i] + a[i+1] <= r):
                a[i+1] += a[i]

    if ans == n:
        print(n)
    else:
        print(ans + 1)


if __name__ == "__main__":
    main()