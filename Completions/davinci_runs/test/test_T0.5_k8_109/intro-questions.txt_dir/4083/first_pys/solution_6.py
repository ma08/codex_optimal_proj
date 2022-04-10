


def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    a.sort()

    if a[0] == a[n - 1]:
        print(0)
        return

    if n == k:
        print(1)
        return

    if k == 1:
        print(a[n - 1] - a[0])
        return

    if a[0] * 2 > a[n - 1]:
        print(-1)
        return

    if n == k + 1:
        if a[0] * 2 <= a[n - 1]:
            print(1)
            return
        else:
            print(-1)
            return

    if a[1] == a[0]:
        print(-1)
        return

    count = 1
    while a[0] * 2 <= a[n - 1]:
        a[0] *= 2
        count += 1

    if a[1] * 2 <= a[n - 1]:
        print(count + 1)
        return

    print(-1)


if __name__ == '__main__':
    main()